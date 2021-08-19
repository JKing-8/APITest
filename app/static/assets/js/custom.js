 jQuery(function($) {


        $(".sidebar-dropdown > a").click(function(){
	        $(".sidebar-submenu").slideUp(250);
        	if ($(this).parent().hasClass("active")){
 		         $(".sidebar-dropdown").removeClass("active");
 		         $(this).parent().removeClass("active");
        	}else{
        		$(".sidebar-dropdown").removeClass("active");
        		$(this).next(".sidebar-submenu").slideDown(250);
        	 	$(this).parent().addClass("active");
        	}

        });
            $(".page-wrapper").click(function (e) {
                var filterList = [
                    $('#toggle-sidebar .fa')
                ]
                var isMenuWrapper = !!$('#sidebar').find($(e.target)).length

debugger
                if(!isMenuWrapper && !filterList.find(item => item.get(0) === e.target) && $('.page-wrapper').attr("class").split(' ').includes('toggled')) {
                     $(".page-wrapper").toggleClass("toggled");
                }

            })
         $("#toggle-sidebar").click(function(){

	         $(".page-wrapper").toggleClass("toggled");

       	 });

           if(! /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
                   $(".sidebar-content").mCustomScrollbar({
                            axis:"y",
                            autoHideScrollbar: true,
                            scrollInertia: 300
                    });
                    $(".sidebar-content").addClass("desktop");

            }
    });