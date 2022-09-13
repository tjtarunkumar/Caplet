/* Theme Name: Ozowkr *
* Developed By: Pratiksha Sharma*
* Version: 1.1, 28 June, 2019*
*/

//Header
		
$('.testimonial-slider').owlCarousel({
	loop: true, 
	margin: 0,
	autoplay: true,
	responsiveClass: true,
	responsive: {
		0: {
			items: 1,
			nav: true
		}, 
		600: {
			items: 3,
			nav: false
		},
		1000: {
			items: 4,
			nav: true,
			loop: true
		}
	}
})

const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);



function increaseCount(a, b) {
  var input = b.previousElementSibling;
  var value = parseInt(input.value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  input.value = value;
}

function decreaseCount(a, b) {
  var input = b.nextElementSibling;
  var value = parseInt(input.value, 10);
  if (value > 1) {
    value = isNaN(value) ? 0 : value;
    value--;
    input.value = value;
  }
}



