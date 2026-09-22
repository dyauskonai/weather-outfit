"use server";

import { headers } from "next/headers";
import { redirect } from "next/navigation";
import { createClient } from "../../lib/supabase/server";
import { getSupabaseConfig } from "../../lib/supabase/config";

function readCredentials(formData: FormData) {
  const email = formData.get("email");
  const password = formData.get("password");

  if (typeof email !== "string" || typeof password !== "string") {
    return null;
  }

  const cleanEmail = email.trim().toLowerCase();

  if (!cleanEmail.includes("@") || password.length < 8) {
    return null;
  }

  return { email: cleanEmail, password };
}

export async function signIn(formData: FormData) {
  if (!getSupabaseConfig()) {
    redirect("/sign-in");
  }

  const credentials = readCredentials(formData);

  if (!credentials) {
    redirect("/sign-in?error=fields");
  }

  const supabase = await createClient();
  const { error } = await supabase.auth.signInWithPassword(credentials);

  if (error) {
    redirect("/sign-in?error=credentials");
  }

  redirect("/dashboard");
}

export async function signUp(formData: FormData) {
  if (!getSupabaseConfig()) {
    redirect("/sign-up");
  }

  const credentials = readCredentials(formData);

  if (!credentials) {
    redirect("/sign-up?error=fields");
  }

  const origin = (await headers()).get("origin") ?? "http://localhost:3000";
  const supabase = await createClient();
  const { data, error } = await supabase.auth.signUp({
    ...credentials,
    options: { emailRedirectTo: new URL("/sign-in", origin).toString() },
  });

  if (error) {
    redirect("/sign-up?error=signup");
  }

  if (data.session) {
    redirect("/dashboard");
  }

  redirect("/sign-in?message=check-email");
}

export async function signOut() {
  if (getSupabaseConfig()) {
    const supabase = await createClient();
    await supabase.auth.signOut();
  }

  redirect("/sign-in");
}
