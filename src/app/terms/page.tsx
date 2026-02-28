"use client";

import React from "react";
import { motion } from "framer-motion";

export default function TermsPage() {
    return (
        <>
            <nav className="navbar">
                <div className="container" style={{ maxWidth: "800px" }}>
                    <a href="/" className="nav-logo">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                            <path d="M12 2L2 22h20L12 2z"></path>
                        </svg>
                        RoomitHosting
                    </a>
                    <ul className="nav-links">
                        <li><a href="/security">Security</a></li>
                        <li><a href="/status">Status</a></li>
                    </ul>
                </div>
            </nav>

            <main>
                <section className="hero" style={{ padding: "8rem 0 4rem", background: "none" }}>
                    <div className="container" style={{ textAlign: "left", maxWidth: "800px" }}>
                        <h1 className="hero-title" style={{ fontSize: "2.5rem", marginBottom: "1rem", textAlign: "left" }}>Terms of Service</h1>
                        <p className="hero-subtitle" style={{ fontSize: "1.125rem", marginLeft: 0, textAlign: "left", maxWidth: "100%" }}>
                            Legal agreements and operational policies governing the use of RoomitHosting infrastructure services.
                        </p>
                    </div>
                </section>

                <section className="section no-border" style={{ paddingTop: 0 }}>
                    <div className="container" style={{ maxWidth: "800px" }}>
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5 }}
                            style={{ display: "flex", flexDirection: "column", gap: "3rem", color: "var(--text-secondary)", lineHeight: 1.7 }}
                        >
                            <div>
                                <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "1rem" }}>1. Scope of Service</h2>
                                <p style={{ marginBottom: "1rem" }}>
                                    RoomitHosting provides managed cloud infrastructure and deployment services. This encompasses the provisioning of computational resources, automated secure socket layer (SSL) configuration, and global edge network distribution according to the plan selected during the deployment request.
                                </p>
                                <p>
                                    The infrastructure is provided "as-is". While we guarantee high availability as per our Service Level Agreements (SLA), the specific performance of individual applications remains subject to the client's codebase optimization.
                                </p>
                            </div>

                            <div>
                                <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "1rem" }}>2. Deployment Responsibility</h2>
                                <p style={{ marginBottom: "1rem" }}>
                                    Clients are exclusively responsible for the functionality, legality, and structural integrity of the application code provided for deployment. RoomitHosting assumes no liability for application-level errors, security vulnerabilities introduced by source code, or regulatory compliance failures originating from the deployed data.
                                </p>
                                <p>
                                    Any deployment found transmitting malicious payloads, engaging in unauthorized network scanning, or violating regional laws will result in immediate infrastructure termination without prior notice.
                                </p>
                            </div>

                            <div>
                                <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "1rem" }}>3. Financial Terms</h2>
                                <p>
                                    Service provisioning is contingent upon successful payment of the one-time infrastructure setup fee. Recurring hosting charges are fundamentally excluded from standard operational contracts unless an ad-hoc enterprise telemetry package is explicitly negotiated. All transactions are securely processed and compliant with regional tax mandates.
                                </p>
                            </div>

                            <div>
                                <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "1rem" }}>4. Refund Policy</h2>
                                <p>
                                    Due to the irreversible resource allocation required to establish edge nodes, provision domain routing, and initialize continuous monitoring, <strong>no refunds are provided after the deployment process has been initiated</strong>. Capital is immediately utilized to reserve infrastructure endpoints specifically tied to the requested deployment domain.
                                </p>
                            </div>

                            <div>
                                <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "1rem" }}>5. Limitation of Liability</h2>
                                <p>
                                    To the maximum extent permitted by applicable law, RoomitHosting shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits, data, use, goodwill, or other intangible losses, resulting from server degradation, network packet loss, or localized edge outages.
                                </p>
                            </div>
                        </motion.div>
                    </div>
                </section>
            </main>

            <footer className="footer" style={{ marginTop: "4rem" }}>
                <div className="container" style={{ maxWidth: "800px" }}>
                    <div className="footer-bottom" style={{ borderTop: "1px solid var(--border-color)", paddingTop: "2rem" }}>
                        <span>© {new Date().getFullYear()} RoomitHosting.</span>
                        <div style={{ display: "flex", gap: "1rem" }}>
                            <a href="/">Return to Platform</a>
                        </div>
                    </div>
                </div>
            </footer>
        </>
    );
}
