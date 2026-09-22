import Link from "next/link";
import WeatherPreview from "./weather-preview";
import AccountMenu from "./account-menu";
import { getCurrentUser } from "../lib/supabase/user";
import styles from "./page.module.css";

const steps = [
  { title: "Start with what you have.", text: "Your favorite top. That Niners jacket. A scarf you knit yourself. A wardrobe that is build around your clothes." },
  { title: "Let the weather weigh in.", text: "Temperature is only part of the story. Warmth, rain, wind, and breathability all guide your decision." },
  { title: "Make getting ready easier.", text: "Get instant recommendations from your wardrobe tailored for comfort." },
];

export default async function Home() {
  const user = await getCurrentUser();

  return (
    <div className={styles.page} id="top">
      <a className={styles.skipLink} href="#main">Skip to content</a>
      <header className={styles.header}>
        <a className={styles.brand} href="#top" aria-label="Weather Outfit home">
          <span className={styles.brandMark} aria-hidden="true">✳</span> Santa Cruz Outfit Recommender
        </a>
        <nav className={styles.nav} aria-label="Main navigation">
          {user ? (
            <AccountMenu email={user.email ?? ""} />
          ) : (
            <Link className={styles.navCta} href="/sign-in">Sign in <span aria-hidden="true">↗</span></Link>
          )}
        </nav>
      </header>
      <main id="main">
        <section className={styles.hero} aria-labelledby="hero-title">
          <div className={styles.atmosphere} aria-hidden="true">
            <div className={styles.orbit} />
            <div className={styles.orbitInner} />
            <div className={styles.grain} />
          </div>
          <div className={styles.heroContent}>
            <p className={styles.eyebrow}><span className={styles.statusDot} /> A little forecast. A better fit.</p>
            <h1 id="hero-title">Your wardrobe.<br /><span>For Santa Cruz.</span></h1>
            <p className={styles.heroDescription}>Less time wondering what to wear.<br />More time getting out there.</p>
            <a className={styles.button} href="#preview">Try it out <span aria-hidden="true">↗</span></a>
            <p className={styles.heroNote}>Built around the clothes you already own.</p>
          </div>
          <div className={styles.forecastStamp} aria-hidden="true">
            <span></span><strong>Make the weather<br />work around you.</strong><span>37° N, 122° W</span>
          </div>
          <div className={styles.heroFooter}><span>YOUR CLOTHES × SC WEATHER</span><a href="#how-it-works">Discover ↓</a></div>
        </section>
        <section className={styles.howSection} id="how-it-works" aria-labelledby="how-title">
          <div className={styles.sectionHeading}>
            <h2 id="how-title">A forecast isn&apos;t sufficient enough.<br /><span>UCSC students need more information.</span></h2>
          </div>
          <div className={styles.steps}>
            {steps.map((step, index) => (
              <article className={styles.step} key={step.title}>
                <span className={styles.stepNumber}>0{index + 1}</span>
                <h3>{step.title}</h3>
                <p>{step.text}</p>
              </article>
            ))}
          </div>
        </section>
        <section className={styles.previewSection} id="preview" aria-labelledby="preview-title">
          <div className={styles.previewIntro}>
            <p className={styles.eyebrow}>A look ahead</p>
            <h2 id="preview-title">Different skies.<br /><span>Different layers.</span></h2>
            <p>Try a change in the weather. See how an outfit could change with it.</p>
            <p className={styles.demoNote}>Interactive Demo. Weather and clothes below are examples, not live forecasts or recommendations from your saved wardrobe.</p>
          </div>
          <WeatherPreview />
        </section>
      </main>
      <footer className={styles.footer}>
        <a className={styles.brand} href="#top"><span className={styles.brandMark} aria-hidden="true">✳</span> santa cruz outfit recommender</a>
        <p>A little more prepared for UCSC</p>
        <a href="#top">Back to top ↑</a>
      </footer>
    </div>
  );
}
