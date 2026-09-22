import { getSupabaseConfig } from "./config";
import { createClient } from "./server";

export async function getCurrentUser() {
  if (!getSupabaseConfig()) {
    return null;
  }

  const supabase = await createClient();
  const { data: { user }, error } = await supabase.auth.getUser();

  return error ? null : user;
}
