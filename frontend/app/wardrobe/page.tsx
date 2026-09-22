import Link from "next/link";
import { redirect } from "next/navigation";
import AccountMenu from "../account-menu";
import { getCurrentUser } from "../../lib/supabase/user";
import styles from "../auth.module.css";

export const dynamic = "force-dynamic";

export default async function WardrobePage() {
  const user = await getCurrentUser();

  if (!user) {
    redirect("/sign-in");
  }

  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <Link className={styles.brand} href="/"><span aria-hidden="true">✳</span> Santa Cruz Outfit Recommender</Link>
        <nav aria-label="Account navigation"><AccountMenu email={user.email ?? ""} /></nav>
      </header>
      <main className={styles.main}>
        <p className={styles.eyebrow}>Your account</p>
        <h1>Your wardrobe.</h1>
        <p className={styles.description}>Your clothing items will appear here after we connect the wardrobe to your account.</p>
        <div className={styles.panel}>Wardrobe tools are coming next.</div>
      </main>
    </div>
  );
}
