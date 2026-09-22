import Link from "next/link";
import { redirect } from "next/navigation";
import { signIn } from "../auth/actions";
import { getSupabaseConfig } from "../../lib/supabase/config";
import { getCurrentUser } from "../../lib/supabase/user";
import styles from "../auth.module.css";

const errorMessages: Record<string, string> = {
  fields: "Enter a valid email and a password of at least 8 characters.",
  credentials: "Could not sign in. Check your email, password, and email confirmation.",
  confirmation: "That confirmation link did not work. Please try signing in or request a new email.",
};

export default async function SignInPage({
  searchParams,
}: {
  searchParams: Promise<{ error?: string; message?: string }>;
}) {
  const { error, message } = await searchParams;
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
        <p className={styles.eyebrow}></p>
        <h1>Welcome back.</h1>
        <p className={styles.description}>Sign in to open your personal wardrobe</p>
        <div className={styles.panel}>
          {!configured && <p className={styles.message}>Account setup is still in progress. A Supabase project URL and publishable key are needed before sign in will work.</p>}
          {error && errorMessages[error] && <p className={styles.message} role="alert">{errorMessages[error]}</p>}
          {message === "check-email" && <p className={styles.message} role="status">Check your email for a confirmation link, then come back to sign in.</p>}
          {configured && (
            <form className={styles.form} action={signIn}>
              <label htmlFor="email">Email</label>
              <input id="email" name="email" type="email" autoComplete="email" placeholder="you@example.com" required />
              <label htmlFor="password">Password</label>
              <input id="password" name="password" type="password" autoComplete="current-password" minLength={8} required />
              <button type="submit">Sign in ↗</button>
            </form>
          )}
          <p className={styles.switch}>New here? <Link href="/sign-up">Create an account</Link></p>
        </div>
      </main>
    </div>
  );
}
