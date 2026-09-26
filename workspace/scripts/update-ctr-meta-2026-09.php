<?php
/**
 * CTR fix — Sep 2026: rewrite Rank Math SEO title + meta description for 5 pages
 * that rank on page 1 but get ~0 clicks (see workspace/reports/ctr-rewrite-2026-09-24.md).
 *
 * Run (live, WordPress.com SSH):  wp eval-file update-ctr-meta-2026-09.php
 * Run (local Studio):             studio.bat wp eval-file wp-content\update-ctr-meta-2026-09.php --path="C:\Users\fatih\Studio\clearlegaltips"
 *
 * Old values are printed first so the change can be rolled back.
 */

$updates = [
	7386 => [
		'title' => 'Statute of Limitations on Debt by State (2026): 3–10 Years',
		'desc'  => 'Debt deadlines for all 50 states + DC: 3 to 10 years on written contracts, often shorter for oral. Check your state before you pay or sue. Verified 2026.',
	],
	1509 => [
		'title' => 'Free Airbnb Rental Agreement Template (2026) + House Rules',
		'desc'  => 'Free short-term rental agreement for Airbnb and VRBO hosts: house rules, quiet hours, damage deposit, and the 30-day rule that turns guests into tenants.',
	],
	5836 => [
		'title' => "Can a Small Business Ask for Donations? Yes, but It's Taxed",
		'desc'  => "Yes, a small business can legally ask for donations, but the money is taxable income and donors can't deduct it. Rules, safe wording, and a free template.",
	],
	1389 => [
		'title' => 'Free Commercial Property Management Agreement Template 2026',
		'desc'  => 'Copy our 15-section commercial property management agreement: fees on collected rent, spending limits, trust accounts, and the broker-license check.',
	],
	5921 => [
		'title' => 'Security Deposit Limits by State (2026): Max & Return Days',
		'desc'  => 'Max security deposit and return deadline for all 50 states + DC. 29 states cap it; deadlines run 10 to 60 days. Miss one and most states charge double.',
	],
];

foreach ( $updates as $pid => $u ) {
	$post = get_post( $pid );
	if ( ! $post ) {
		echo "SKIP $pid: post not found\n";
		continue;
	}
	echo "== $pid {$post->post_name}\n";
	echo "  OLD title: " . get_post_meta( $pid, 'rank_math_title', true ) . "\n";
	echo "  OLD desc : " . get_post_meta( $pid, 'rank_math_description', true ) . "\n";

	update_post_meta( $pid, 'rank_math_title', $u['title'] );
	update_post_meta( $pid, 'rank_math_description', $u['desc'] );
	clean_post_cache( $pid );

	echo "  NEW title: {$u['title']}\n";
	echo "  NEW desc : {$u['desc']}\n";
}
