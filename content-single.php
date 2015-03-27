<?php
/**
 * @package pythonbeginner
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<header class="entry-header">
		<?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>

		<div class="entry-meta">
			<?php pythonbeginner_posted_on(); ?>
		</div><!-- .entry-meta -->
        <hr/>
	</header><!-- .entry-header -->

	<div class="entry-content">
        <?php the_post_thumbnail(); ?>

		<?php the_content(); ?>
		<?php
			wp_link_pages( array(
				'before' => '<div class="page-links">' . __( 'Pages:', 'pythonbeginner' ),
				'after'  => '</div>',
			) );
		?>
	</div><!-- .entry-content -->

	<footer class="entry-footer">
		<?php pythonbeginner_entry_footer(); ?>
	</footer><!-- .entry-footer -->
</article><!-- #post-## -->
