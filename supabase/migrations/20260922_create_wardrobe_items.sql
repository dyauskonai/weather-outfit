-- Supabase Auth already owns auth.users. Each clothing row belongs to one of those users.
create table public.wardrobe_items (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
    name text not null check (char_length(trim(name)) between 1 and 120),
    category text not null check (category in ('top', 'outerwear', 'bottom', 'footwear')),
    primary_purpose text not null check (primary_purpose in ('general', 'warmth', 'rain')),
    warmth numeric(3, 2) not null check (warmth between 0 and 1),
    rain_protection numeric(3, 2) not null check (rain_protection between 0 and 1),
    wind_protection numeric(3, 2) not null check (wind_protection between 0 and 1),
    breathability numeric(3, 2) not null check (breathability between 0 and 1),
    created_at timestamptz not null default now()
);

create index wardrobe_items_user_id_idx on public.wardrobe_items (user_id);

alter table public.wardrobe_items enable row level security;
revoke all on table public.wardrobe_items from anon, authenticated;
grant select, insert, update, delete on table public.wardrobe_items to authenticated;

create policy "Read own wardrobe"
on public.wardrobe_items for select to authenticated
using ((select auth.uid()) = user_id);

create policy "Add to own wardrobe"
on public.wardrobe_items for insert to authenticated
with check ((select auth.uid()) = user_id);

create policy "Edit own wardrobe"
on public.wardrobe_items for update to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

create policy "Remove from own wardrobe"
on public.wardrobe_items for delete to authenticated
using ((select auth.uid()) = user_id);
