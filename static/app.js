<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.js"></script>
<script>

    var photo = "{{ my }}";

    $(document).scroll(function () {

        var maxHeight = $(document).height();
        var currentScroll = $(window).scrollTop() + $(window).height();

        if (maxHeight <= currentScroll + 100) {
            $("body").append('<div class="big-box"><h1>Page</h1></div>');
            $("body").append('<div class="big-box"><h1>Page</h1></div>');
        }
    });
</script>