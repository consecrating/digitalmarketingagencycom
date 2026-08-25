/***************************************************
==================== About Template ======================
****************************************************

    Theme Name: Ranko - SEO & Digital Marketing HTML5 Template
		Theme URI: https://themejunction.net/html/ranko/demo/
    Author: Theme-Junction
		Author URI: https://themeforest.net/user/theme-junction
    Support: https://support.themejunction.net/
    Description: Ranko - SEO & Digital Marketing HTML5 Template
    Version: 1.0

****************************************************/

/***************************************************
==================== JS INDEX ======================
****************************************************

1. Preloader
2. WOW Animation
3. Backtotop
4. Sticky header
5. Mobile Menu Js
6. Offcanvas
7. Hamburger Menu
8. GSAP Registratiobn
9. Progress bar
10. Nice select
11. Marquee slide
12. Slider
13. Odometer
14. Tab controller
15. Glightbox Gallery
16. Rating
17. Title Animation

****************************************************/

(function ($) {
	"use strict";
	/*====================== Preloader ======================*/
	$(window).on("load", function () {
		const tjPreloader = $(".preloader");
		otherScriptsController();
		if (tjPreloader?.length) {
			tjPreloader.fadeOut(300);
			wowController();
			gsapController();
		} else {
			wowController();
			gsapController();
		}
	});

	/*====================== WOW Animation ======================*/
	function wowController() {
		var wow = new WOW({
			boxClass: "wow", // default
			animateClass: "animated", // default
			offset: 20, // default
			callback: function (box) {
				// Ensure visibility when animation starts
				$(box).css("visibility", "visible");
				$(box).css("opacity", "1");
			},
		});
		wow.init();
	}

	/*====================== GSAP Animation ======================*/
	function gsapController() {
		/*====================== GSAP Registratiobn ======================*/
		gsap.registerPlugin(
			ScrollTrigger,
			ScrollSmoother,
			SplitText,
			TweenMax,
			ScrollToPlugin
		);
		// Scroll Smother
		if ($("#smooth-wrapper").length && $("#smooth-content").length) {
			gsap.config({
				nullTargetWarn: false,
			});
			let smoother = ScrollSmoother.create({
				smooth: 1.5,
				effects: true,
				smoothTouch: 0.1,
				ignoreMobileResize: true,
			});
		}
		// common variable and funtion
		let mediaMatch = gsap.matchMedia();
		function rtlValue(value) {
			const isRTL = document.documentElement.dir === "rtl";
			return isRTL ? -value : value;
		}

		// Onepage navigation
		const tjScrollButton = document.querySelectorAll(".tj-scroll-btn");
		if (tjScrollButton?.length) {
			tjScrollButton.forEach((btn, index) => {
				btn.addEventListener("click", () => {
					var sectionTarget = btn.getAttribute("data-target");
					gsap.to(window, {
						duration: 0.3,
						scrollTo: { y: sectionTarget, offsetY: 70 },
					});
				});
			});
		}

		// Title Animation
		if ($(".title-animation").length) {
			let animatedTextElements = document.querySelectorAll(".title-animation");

			animatedTextElements.forEach(element => {
				//Reset if needed
				if (element.animation) {
					element.animation.progress(1).kill();
					element.split.revert();
				}

				element.split = new SplitText(element, {
					type: "lines,words,chars",
					linesClass: "split-line",
				});
				gsap.set(element, { perspective: 400 });

				gsap.set(element.split.chars, {
					opacity: 0,
					x: "50",
				});

				element.animation = gsap.to(element.split.chars, {
					scrollTrigger: { trigger: element, start: "top 90%" },
					x: "0",
					y: "0",
					rotateX: "0",
					opacity: 1,
					duration: 1,
					ease: Back.easeOut,
					stagger: 0.02,
				});
			});
		}

		/* Title Animation 2 */
		if ($(".title-animation-2").length) {
			let staggerAmount = 0.01,
				delayValue = 0.1,
				easeType = "power1.inOut",
				animatedTitleElements = document.querySelectorAll(".title-animation-2");
			animatedTitleElements.forEach(element => {
				let split = new SplitText(element, {
					types: "lines, words, chars",
				});
				const immediateDivs = element.querySelectorAll(":scope > div");
				// Set initial overflow hidden
				immediateDivs.forEach(div => (div.style.overflow = "hidden"));
				gsap.from(split.chars, {
					y: "100%",
					duration: 0.5,
					delay: delayValue,
					autoAlpha: 0,
					stagger: staggerAmount,
					ease: easeType,
					scrollTrigger: {
						trigger: element,
						start: "top 85%",
						onEnter: () => {
							// Ensure it's hidden before animation starts
							immediateDivs.forEach(div => (div.style.overflow = "hidden"));
						},
					},
					onComplete: () => {
						// Now it runs right after animation finishes
						immediateDivs.forEach(div => (div.style.overflow = "visible"));
					},
				});
			});
		}

		// Text Highlight
		if ($(".title-highlight").length) {
			const highlightText = new SplitText(".title-highlight", {
				type: "lines",
				linesClass: "line",
			});

			const tl = gsap.timeline({
				scrollTrigger: {
					trigger: ".title-highlight",
					scrub: 1,
					start: "top 80%",
					end: "bottom center",
				},
			});
			tl.to(".line", {
				"--highlight-offset": "100%",
				stagger: 0.4,
			});
		}

		// Right Swipe
		document.querySelectorAll(".rightSwipeWrap").forEach((wrap, i) => {
			gsap.set(wrap.querySelectorAll(".right-swipe"), {
				transformPerspective: 1200,
				x: "10rem",
				rotateY: -20,
				opacity: 0,
				transformOrigin: "right center",
			});
			gsap.to(wrap.querySelectorAll(".right-swipe"), {
				transformPerspective: 1200,
				x: 0,
				rotateY: 0,
				opacity: 1,
				delay: 0.3,
				ease: "power3.out",
				scrollTrigger: {
					trigger: wrap,
					start: "top 80%",
					id: "rightSwipeWrap-" + i,
					toggleActions: "play none none none",
					// markers: true,
				},
			});
		});

		// Left Swipe
		document.querySelectorAll(".leftSwipeWrap").forEach((wrap, i) => {
			gsap.set(wrap.querySelectorAll(".left-swipe"), {
				transformPerspective: 1200,
				x: "-10rem",
				rotateY: 20,
				opacity: 0,
				transformOrigin: "left center",
			});
			gsap.to(wrap.querySelectorAll(".left-swipe"), {
				transformPerspective: 1200,
				x: 0,
				rotateY: 0,
				opacity: 1,
				delay: 0.4,
				ease: "power3.out",
				scrollTrigger: {
					trigger: wrap,
					start: "top 80%",
					id: "leftSwipeWrap-" + i,
					toggleActions: "play none none none",
					// markers: true,
				},
			});
		});

		// Progress bar
		const progressBarController = () => {
			const progressContainers = document.querySelectorAll(".tj-progress");
			if (progressContainers?.length) {
				progressContainers.forEach(progressContainer => {
					const targetedProgressBar =
						progressContainer.querySelector(".tj-progress__bar");
					const completedPercent =
						parseInt(targetedProgressBar.getAttribute("data-perchant"), 10) ||
						0;

					gsap.to(targetedProgressBar, {
						width: `${completedPercent}%`, // Correct width
						ease: "power2.out",
						scrollTrigger: {
							trigger: progressContainer, // Use container for better scroll handling
							start: "top 90%",
							end: "top 30%",
						},
						onUpdate: function () {
							let progressValue = Math.round(this.progress() * 100); // Corrected scaling
							let displayPercent = Math.round(
								(completedPercent * progressValue) / 100
							); // Fixes low % issue

							const percentageText = progressContainer.querySelector(
								".tj-progress__perchant"
							);
							if (percentageText) {
								percentageText.textContent = displayPercent + "%";
							}
						},
					});
				});
			}
		};
		progressBarController();

		// Stack with Scale Down
		const serviceStack = gsap.utils.toArray(".tj-stack");
		if (serviceStack.length > 0) {
			mediaMatch.add("(min-width: 992px)", () => {
				serviceStack.forEach(item => {
					gsap.to(item, {
						opacity: 0,
						scale: 0.9,
						y: 50,
						scrollTrigger: {
							trigger: item,
							scrub: true,
							start: "top top",
							pin: true,
							pinSpacing: false,
							markers: false,
						},
					});
				});
			});
		}

		// sticky Pannels
		function initStickyPanelAnimation() {
			const container = document.querySelector(".tj-sticky-panel-container");
			const panels = document.querySelectorAll(".tj-sticky-panel");
			if (!container || panels.length === 0) return;
			mediaMatch.add("(min-width: 992px)", () => {
				const startOffset =
					parseInt(getComputedStyle(container).paddingTop, 10) || 0;
				const stackDifference = 75;
				const lastIdx = panels.length - 1;
				const lastPanel = panels[lastIdx];
				const paddingBottom =
					parseInt(getComputedStyle(container).paddingBottom, 10) || 0;
				panels.forEach((panel, i) => {
					const extraStartingOffset =
						i === 0 || i === 1 ? 0 : (i - 1) * stackDifference;
					gsap.to(panel, {
						scrollTrigger: {
							trigger: panel,
							start: `top-=${startOffset + extraStartingOffset} top`,
							endTrigger: container,
							end: () =>
								`bottom top+=${
									lastPanel.offsetHeight +
									startOffset +
									paddingBottom +
									(lastIdx - 1) * stackDifference
								}`,
							pin: true,
							pinSpacing: false,
							scrub: true,
							markers: false,
							invalidateOnRefresh: true,
						},
						ease: "circ",
					});
				});
			});
		}
		initStickyPanelAnimation();

		// sticky Pannels 2
		function initStickyPanelAnimation2() {
			const container = document.querySelector(".tj-sticky-panel-container-2");
			const panels = document.querySelectorAll(".tj-sticky-panel-2");
			if (!container || panels.length === 0) return;
			mediaMatch.add("(min-width: 992px)", () => {
				const startOffset = 60 || 0;
				const stackDifference = 0;
				const lastIdx = panels.length - 1;
				const lastPanel = panels[lastIdx];
				const paddingBottom =
					parseInt(getComputedStyle(container).paddingBottom, 10) || 0;
				panels.forEach((panel, i) => {
					const extraStartingOffset = i * stackDifference;
					gsap.to(panel, {
						scrollTrigger: {
							trigger: panel,
							start: `top-=${startOffset + extraStartingOffset} top`,
							endTrigger: container,
							end: () =>
								`bottom top+=${
									lastPanel.offsetHeight +
									startOffset +
									paddingBottom +
									lastIdx * stackDifference
								}`,
							pin: true,
							pinSpacing: false,
							scrub: true,
							markers: false,
							invalidateOnRefresh: true,
						},
						ease: "circ",
					});
				});
			});
		}
		initStickyPanelAnimation2();

		// Sidebar sticky
		function sidebarStickyController() {
			const containers = document.querySelectorAll(
				".slidebar-stickiy-container"
			);
			if (containers.length) {
				containers.forEach(container => {
					const panels = container.querySelectorAll(".slidebar-stickiy");
					if (panels.length) {
						mediaMatch.add("(min-width: 992px)", () => {
							const startOffset = 30;
							//parseInt(getComputedStyle(container).paddingTop) || 0;
							const lastIdx = panels.length - 1;
							const lastPanel = panels[lastIdx];
							const paddingBottom =
								parseInt(getComputedStyle(container).paddingBottom) || 0;
							panels.forEach((panel, i) => {
								gsap.to(panel, {
									scrollTrigger: {
										trigger: panel,
										start: `top-=${startOffset} top`,
										endTrigger: container,
										end: () =>
											`bottom top+=${
												lastPanel.offsetHeight + startOffset + paddingBottom
											}`,
										pin: true,
										pinSpacing: false,
										scrub: true,
										markers: false,
										invalidateOnRefresh: true,
									},
									ease: "circ",
								});
							});
						});
					}
				});
			}
		}
		sidebarStickyController();

		// Scroll Progress Animation
		if ($(".tj-progress-item").length > 0) {
			let mediaMatch = gsap.matchMedia();
			mediaMatch.add("(min-width: 992px)", () => {
				const slider = document.querySelector(".tj-progress-wrapper");

				if (slider?.children?.length) {
					let panels = gsap.utils.toArray(".tj-progress-item");
					let mockupItems = gsap.utils.toArray(".process-mockup-item");
					let totalPanels = panels.length;

					gsap.to(panels, {
						ease: "none",
						scrollTrigger: {
							trigger: slider,
							start: "top+=220 top",
							pin: true,
							scrub: 1,
							end: "+=700",

							onUpdate: self => {
								// Keep your original panel animation logic
								let progress = self.progress;
								let progressModified = progress * (totalPanels - 1);
								let activeIndex = Math.round(progressModified);

								panels.forEach((panel, index) => {
									panel.classList.toggle("active", index === activeIndex);
								});

								// Smooth transform control for mockup items
								mockupItems.forEach((item, index) => {
									if (index === 0) {
										// #1 always sticky, no movement
										item.classList.add("sticky");
										gsap.to(item, { yPercent: 0, duration: 0.3, ease: "none" });
									}
									if (index === 1) {
										// #2 moves from 0 → -100% over middle 1/3 of scroll
										let p = gsap.utils.clamp(0, 1, (progress - 0.33) / 0.33);
										let yValue = -100 * p;
										item.classList.add("sticky");
										gsap.to(item, {
											yPercent: yValue,
											duration: 0.2,
											ease: "none",
										});
									}
									if (index === 2) {
										// #3 moves from 0 → -200% over last 1/3 of scroll
										let p = gsap.utils.clamp(0, 1, (progress - 0.66) / 0.34);
										let yValue = -200 * p;
										item.classList.add("sticky");
										gsap.to(item, {
											yPercent: yValue,
											duration: 0.2,
											ease: "none",
										});
									}
								});
							},
						},
					});
				}
			});
		}
	}

	/*====================== All Other Scripts ======================*/
	function otherScriptsController() {
		// Data Js
		$("[data-bg-image]").each(function () {
			$(this).css(
				"background-image",
				"url(" + $(this).attr("data-bg-image") + ")"
			);
		});

		/*====================== Backtotop ======================*/
		function back_to_top() {
			if ($("#back_to_top").length) {
				var btn = $("#back_to_top");
				var btn_wrapper = $(".back-to-top-wrapper");

				$(window).on("scroll", function () {
					if ($(window).scrollTop() > 300) {
						btn_wrapper.addClass("back-to-top-btn-show");
					} else {
						btn_wrapper.removeClass("back-to-top-btn-show");
					}
				});

				btn.on("click", function (e) {
					e.preventDefault();
					$("html, body").animate({ scrollTop: 0 }, "300");
				});
			}
		}
		back_to_top();

		/*====================== Sticky header ======================*/
		let lastScrollTop = 0;
		const header = document.querySelector(".header-sticky");
		window.addEventListener("scroll", function () {
			let scrollTop = window.scrollY || document.documentElement.scrollTop;
			if (scrollTop > lastScrollTop || scrollTop < 400) {
				// Scrolling Down
				header.classList.remove("sticky");
			} else {
				// Scrolling Up
				header.classList.add("sticky");
			}

			lastScrollTop = scrollTop;
		});

		/*====================== Mobile Menu Js ======================*/
		$(".menu_bar").on("click", function () {
			$(this).toggleClass("on");
		});

		/*====================== Offcanvas ======================*/
		$(".menu_bar.menu_offcanvas").on("click", function () {
			$(".tj-offcanvas-area").toggleClass("opened");
			$("body").toggleClass("overflow-hidden");
		});
		$("#mobileNavProvider").meanmenu({
			meanMenuContainer: ".mobile_menu",
			meanScreenWidth: "991",
			meanExpand: ['<i class="tji-arrow-down-filled"></i>'],
		});

		/*====================== Hamburger Menu ======================*/
		$(".mobile_menu_bar").on("click", function () {
			$(".hamburger-area").addClass("opened");
			$(".body-overlay").addClass("opened");
		});
		$(".hamburger_close_btn").on("click", function () {
			$(".hamburger-area").removeClass("opened");
			$(".body-overlay").removeClass("opened");
			$(".mobile_menu_bar").removeClass("on");
		});
		$(".body-overlay").on("click", function () {
			$(".hamburger-area").removeClass("opened");
			$(".body-overlay").removeClass("opened");
			$(".mobile_menu_bar").removeClass("on");
		});

		/*====================== Nice Select ======================*/
		if ($(".tj-nice-select").length) {
			$(".tj-nice-select").niceSelect();
		}

		/*====================== Marquee Slider ======================*/
		//Brand Marquue Js
		if ($(".brand-marquee__slider").length > 0) {
			var marquee = new Swiper(".brand-marquee__slider", {
				slidesPerView: "auto",
				spaceBetween: 0,
				freemode: true,
				centeredSlides: true,
				loop: true,
				speed: 4000,
				allowTouchMove: false,
				autoplay: {
					delay: 0,
				},
				breakpoints: {
					1200: {
						spaceBetween: 23,
					},
				},
			});
		}
		// Client-slider Js
		if ($(".client-slider").length > 0) {
			var client = new Swiper(".client-slider", {
				slidesPerView: "auto",
				spaceBetween: 0,
				freemode: true,
				centeredSlides: true,
				loop: true,
				speed: 5000,
				allowTouchMove: false,
				autoplay: {
					delay: 1,
					disableOnInteraction: true,
				},
			});
		}
		//Service Marquee
		if ($(".service-marquee__slider").length > 0) {
			var marquee = new Swiper(".service-marquee__slider", {
				slidesPerView: "auto",
				spaceBetween: 20,
				freemode: true,
				centeredSlides: true,
				loop: true,
				speed: 4000,
				allowTouchMove: false,
				autoplay: {
					delay: 0,
				},
				breakpoints: {
					1200: {
						spaceBetween: 50,
					},
					992: {
						spaceBetween: 40,
					},
					768: {
						spaceBetween: 30,
					},
				},
			});
		}
		//Text Marquee
		if ($(".text-marquee-slider").length > 0) {
			var marquee = new Swiper(".text-marquee-slider", {
				slidesPerView: "auto",
				spaceBetween: 10,
				freemode: true,
				centeredSlides: true,
				loop: true,
				speed: 4000,
				allowTouchMove: false,
				autoplay: {
					delay: 0,
				},
				breakpoints: {
					1200: {
						spaceBetween: 20,
					},
				},
			});
		}
		// feature marquee
		if ($(".tj__marquee__slider").length > 0) {
			var swiper = new Swiper(".tj__marquee__slider", {
				slidesPerView: "auto",
				spaceBetween: 30,
				loop: true,
				speed: 5000,
				breakpoints: {
					768: {
						spaceBetween: 35,
					},

					1024: {
						spaceBetween: 40,
					},
				},
				allowTouchMove: false,
				autoplay: {
					delay: 1,
					disableOnInteraction: true,
				},
			});
		}

		/*====================== Slider ======================*/
		// Portfolio Slider
		if (document.querySelector(".portfolio__slider")) {
			var swiper = new Swiper(".portfolio__slider", {
				slidesPerView: 1.3,
				spaceBetween: 20,
				centeredSlides: true,
				loop: true,
				initialSlide: 2,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				breakpoints: {
					1200: {
						slidesPerView: 4,
						spaceBetween: 30,
					},
					992: {
						slidesPerView: 4,
						spaceBetween: 20,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		// Portfolio 2 Slider
		if (document.querySelector(".portfolio__slider__2")) {
			var swiper = new Swiper(".portfolio__slider__2", {
				slidesPerView: 1.3,
				spaceBetween: 20,
				centeredSlides: true,
				loop: true,
				initialSlide: 2,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				breakpoints: {
					576: {
						slidesPerView: 1.5,
					},
					992: {
						slidesPerView: 2,
						spaceBetween: 30,
					},
					1200: {
						slidesPerView: 2.5,
					},
					1600: {
						slidesPerView: 4,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		// Portfolio 2 Slider
		if (document.querySelector(".portfolio__slider__3")) {
			var swiper = new Swiper(".portfolio__slider__3", {
				slidesPerView: 1.2,
				spaceBetween: 20,
				centeredSlides: true,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				breakpoints: {
					992: {
						centeredSlides: false,
						slidesPerView: 2,
						spaceBetween: 30,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		// Testimonials Slider
		if (document.querySelector(".testimonials__slider")) {
			var swiper = new Swiper(".testimonials__slider", {
				slidesPerView: 1,
				spaceBetween: 20,
				loop: true,
				initialSlide: 1,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				breakpoints: {
					992: {
						slidesPerView: 2,
						spaceBetween: 30,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		// Testimonials 2 Slider
		if (document.querySelector(".testimonials__slider__2")) {
			var swiper = new Swiper(".testimonials__slider__2", {
				slidesPerView: 1.2,
				spaceBetween: 20,
				centeredSlides: true,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				breakpoints: {
					992: {
						centeredSlides: false,
						slidesPerView: 2,
						spaceBetween: 30,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		// Testimonials 3 Slider
		if (document.querySelector(".testimonials__slider__3")) {
			var swiperTumbs = new Swiper(".testimonials__slider__3__thumbs", {
				spaceBetween: 30,
				slidesPerView: 1,
				loop: true,
				freeMode: true,
				watchSlidesProgress: true,
				speed: 5000,
				effect: "fade",
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},
			});
			var swiperSlider3 = new Swiper(".testimonials__slider__3", {
				spaceBetween: 30,
				slidesPerView: 1,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".testimonials-nav-next",
					prevEl: ".testimonials-nav-prev",
				},
			});

			swiperSlider3.controller.control = swiperTumbs;
			swiperTumbs.controller.control = swiperSlider3;
		}
		// Testimonials 4 Slider
		if (document.querySelector(".testimonials__slider__4")) {
			var swiperSlider3 = new Swiper(".testimonials__slider__4", {
				spaceBetween: 0,
				slidesPerView: 1,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
			});
		}
		// Hero Testimonials 5 Slider
		if (document.querySelector(".testimonials__slider__5")) {
			var swiper = new Swiper(".testimonials__slider__5", {
				slidesPerView: 1,
				spaceBetween: 20,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 7000,
					disableOnInteraction: true,
				},

				breakpoints: {
					768: {
						slidesPerView: 2,
						spaceBetween: 30,
					},
					1200: {
						slidesPerView: 3,
						spaceBetween: 30,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		//  Testimonial Slider
		if ($(".hero__analytics__slider__main").length > 0) {
			var slider = new Swiper(".hero__analytics__slider__main", {
				direction: "vertical",
				slidesPerView: "auto",
				spaceBetween: 15,
				allowTouchMove: false,
				loop: true,
				speed: 1000,
				autoplay: {
					delay: 5000,
				},

				breakpoints: {
					992: {
						spaceBetween: 22,
					},
				},
			});
		}
		// Team Slider
		if ($(".team__slider").length > 0) {
			var slider = new Swiper(".team__slider", {
				slidesPerView: 2,
				spaceBetween: 15,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 5000,
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},

				breakpoints: {
					576: {
						slidesPerView: 2,
					},
					992: {
						slidesPerView: 3,
						spaceBetween: 30,
					},
					1200: {
						slidesPerView: 4,
					},
				},
			});
		}
		// Tab Slider
		if (document.querySelector(".strategy__tab__slider")) {
			var swiper = new Swiper(".strategy__tab__slider", {
				slidesPerView: 2,
				spaceBetween: 15,

				breakpoints: {
					768: {
						slidesPerView: 3,
						spaceBetween: 16,
					},
					992: {
						slidesPerView: 4,
					},
					1200: {
						spaceBetween: 20,
						slidesPerView: 4,
					},
					1440: {
						slidesPerView: 5,
						spaceBetween: 20,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}
		// Service Slider
		if (document.querySelector(".service__slider")) {
			var swiper = new Swiper(".service__slider", {
				slidesPerView: 1.3,
				spaceBetween: 20,
				centeredSlides: true,
				loop: true,
				initialSlide: 2,
				speed: 1500,
				autoplay: {
					delay: 3000,
					disableOnInteraction: true,
				},

				breakpoints: {
					1400: {
						slidesPerView: 4,
						spaceBetween: 30,
					},
					1200: {
						slidesPerView: 3.15,
						spaceBetween: 30,
					},
					992: {
						slidesPerView: 2.6,
						spaceBetween: 20,
					},
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
			});
		}

		// Testimonial 6 Slider Js
		if (
			$(".testimonials__author__slider").length > 0 &&
			$(".testimonials__slider__6").length > 0
		) {
			let thumbSlider = new Swiper(".testimonials__author__slider", {
				slidesPerView: 3,
				spaceBetween: 12,
				loop: true,
				speed: 1500,
				centeredSlides: true,
				freeMode: true,
				watchSlidesProgress: true,
				slideToClickedSlide: true,
			});

			let testimonialSlider = new Swiper(".testimonials__slider__6", {
				slidesPerView: 1.2,
				spaceBetween: 30,
				centeredSlides: true,
				loop: true,
				speed: 1500,
				autoplay: {
					delay: 3000,
				},
				navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				},
				pagination: {
					el: ".swiper-pagination",
					clickable: true,
				},
				breakpoints: {
					0: {
						slidesPerView: 1.001,
						spaceBetween: 15,
					},
					576: {
						slidesPerView: 1.1,
						spaceBetween: 15,
					},
					768: {
						slidesPerView: 1.2,
						spaceBetween: 20,
					},
					992: {
						slidesPerView: 1.25,
						spaceBetween: 25,
					},
					1200: {
						slidesPerView: 1.28,
						spaceBetween: 30,
					},
				},
			});

			// Connect the sliders
			testimonialSlider.controller.control = thumbSlider;
			thumbSlider.controller.control = testimonialSlider;
		}

		/*====================== Odometer ======================*/
		function controllOdometer(num) {
			if ($(".number .odometer").length > 0) {
				if (num === 2) {
					$(`.number--${num} .odometer`).each(function () {
						var countNumber = $(this).attr("data-count");
						$(this).html(countNumber);
					});
				} else {
					$(`.number:not(.number--2) .odometer`).each(function () {
						var $this = $(this);
						$this.appear(
							function () {
								var countNumber = $this.attr("data-count");
								$this.html(countNumber);
							},
							{ accX: 0, accY: -100 }
						);
					});
				}
			}
		}
		controllOdometer(1);

		/*====================== Tab Controller ======================*/
		$(".tj-tab-switcher__controller").on("change", function () {
			if ($(this).prop("checked")) {
				$("#tab1").removeClass("show active");
				$("#tab2").addClass("show active");
				controllOdometer(2);
			} else {
				$("#tab2").removeClass("show active");
				$("#tab1").addClass("show active");
			}
		});

		/*====================== Glightbox Gallery ======================*/
		function tjGalleryFunc(selector, effect) {
			if (document.querySelector(`.${selector}`)) {
				const lightbox = GLightbox({
					selector: `.${selector}`,
					width: "70vw",
					openEffect: effect || "zoom",
					slideEffect: "fade",
					loop: true,
				});
			}
		}
		tjGalleryFunc("tj-gallery-item");

		/*====================== Rating ======================*/
		const starRatings = $(".star-ratings");
		if ($(".fill-ratings span").length > 0) {
			starRatings.each(function () {
				var $star = $(this);
				var $fill = $star.find(".fill-ratings span");
				if ($fill.length > 0) {
					var fillWidth = $fill.width();
					$star.width(fillWidth);
				}
			});
		}
		/*====================== Hover Active ======================*/
		const hoverActiveWrappers = document.querySelectorAll(
			".hover-active-wrapper"
		);
		if (hoverActiveWrappers.length) {
			hoverActiveWrappers.forEach((hoverActiveWrapper, idx) => {
				const items = hoverActiveWrapper.querySelectorAll(".hover-active-item");
				if (items.length) {
					items.forEach(item => {
						item.addEventListener("mouseenter", function () {
							items.forEach(item2 => {
								item2.classList.remove("active");
							});
							this.classList.add("active");
						});
					});
				}
			});
		}

		/*====================== Circle Proggess Bar  ======================*/
		if (typeof $.fn.knob != "undefined") {
			$(".knob").each(function () {
				var $this = $(this),
					knobVal = $this.attr("data-rel");

				$this.knob({
					draw: function () {
						$(this.i).val(this.cv + "%");
					},
				});

				$this.appear(
					function () {
						$({
							value: 0,
						}).animate(
							{
								value: knobVal,
							},
							{
								duration: 2000,
								easing: "swing",
								step: function () {
									$this.val(Math.ceil(this.value)).trigger("change");
								},
							}
						);
					},
					{
						accX: 0,
						accY: -150,
					}
				);
			});
		}

		/*====================== Image Reveal Animation ======================*/
		const revealParentElements = document.querySelectorAll(
			".tj-reveal-img-wrapper"
		);
		if (revealParentElements?.length) {
			function moveImage(e, revealParentElement, index) {
				const item = revealParentElement.getBoundingClientRect();
				const x = e.clientX - item.x;
				const y = e.clientY - item.y;
				const revealImgeElement =
					revealParentElement?.querySelector(".tj-reveal-img");
				if (revealImgeElement) {
					revealImgeElement.style.transform = `translate(${x}px, ${y}px)`;
				}
			}
			revealParentElements.forEach((item, i) => {
				item.addEventListener("mousemove", e => {
					setInterval(moveImage(e, item, 1), 50);
				});
			});
		}
	}
})(jQuery);
