import Link from "next/link";
import { redirect } from "next/navigation";
import { signUp } from "../auth/actions";
import { getSupabaseConfig } from "../../lib/supabase/config";
import { getCurrentUser } from "../../lib/supabase/user";
import styles from "../auth.module.css";

export default async function SignUpPage({
  searchParams,
}: {
  searchParams: Promise<{ error?: string }>;
}) {
  const { error } = await searchParams;
  const configured = Boolean(getSupabaseConfig());
  const user = await getCurrentUser();

  if (user) {
    redirect("/dashboard");
  }

  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <Link className={styles.brand} href="/"><span aria-hidden="true">✳</span> Santa Cruz Outfit Recommender</Link>
        <Link className={styles.back} href="/">← Home</Link>
      </header>
      <main className={styles.main}>
        <p className={styles.eyebrow}>Make it yours</p>
        <h1>Create an account.</h1>
        <p className={styles.description}>Your account will give your wardrobe its own private home as we build the next part of the app.</p>
        <div className={styles.panel}>
          {!configured && <p className={styles.message}>Account setup is still in progress. Add your Supabase project settings to enable sign up.</p>}
          {error === "fields" && <p className={styles.message} role="alert">Enter a valid email and a password of at least 8 characters.</p>}
          {error === "signup" && <p className={styles.message} role="alert">We could not create the account. Check the details and try again.</p>}
          {configured && (
            <form className={styles.form} action={signUp}>
              <label htmlFor="email">Email</label>
              <input id="email" name="email" type="email" autoComplete="email" placeholder="you@example.com" required />
              <label htmlFor="password">Password</label>
              <input id="password" name="password" type="password" autoComplete="new-password" minLength={8} required />
              <button type="submit">Create account ↗</button>
            </form>
          )}
          <p className={styles.switch}>Already have an account? <Link href="/sign-in">Sign in</Link></p>
        </div>
      </main>
    </div>
  );
}
