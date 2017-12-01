$(function () {
    $(document).scroll(function () {

        var maxHeight = $(document).height();
        var currentScroll = $(window).scrollTop() + $(window).height();

        if (typeof arr[i] != "undefined") {
            if (maxHeight <= currentScroll + 400) {
                if (mode == 0) {

                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i] + '" download><img src="../static/images/' + arr[i] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 1] + '" download><img src="../static/images/' + arr[i + 1] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 2] + '" download><img src="../static/images/' + arr[i + 2] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 3] + '" download><img src="../static/images/' + arr[i + 3] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 4] + '" download><img src="../static/images/' + arr[i + 4] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 5] + '" download><img src="../static/images/' + arr[i + 5] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 6] + '" download><img src="../static/images/' + arr[i + 6] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 7] + '" download><img src="../static/images/' + arr[i + 7] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 8] + '" download><img src="../static/images/' + arr[i + 8] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 9] + '" download><img src="../static/images/' + arr[i + 9] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 10] + '" download><img src="../static/images/' + arr[i + 10] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 11] + '" download><img src="../static/images/' + arr[i + 11] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);

                    i += 12;
                }
                else {
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i] + '" download><img src="../static/images/' + gif[i] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 1] + '" download><img src="../static/images/' + gif[i + 1] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 2] + '" download><img src="../static/images/' + gif[i + 2] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 3] + '" download><img src="../static/images/' + gif[i + 3] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 4] + '" download><img src="../static/images/' + gif[i + 4] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 5] + '" download><img src="../static/images/' + gif[i + 5] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 6] + '" download><img src="../static/images/' + gif[i + 6] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 7] + '" download><img src="../static/images/' + gif[i + 7] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 8] + '" download><img src="../static/images/' + gif[i + 8] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 9] + '" download><img src="../static/images/' + gif[i + 9] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 10] + '" download><img src="../static/images/' + gif[i + 10] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 11] + '" download><img src="../static/images/' + gif[i + 11] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);

                    i += 12;
                }
            }
        }

        var maxHeight2 = -1;

        $('.overzoom').each(function () {
            maxHeight2 = maxHeight2 > $(this).height() ? maxHeight2 : $(this).height();
        });

        $('.overzoom').each(function () {
            $(this).height(maxHeight2);
        });

        $('img').flexVerticalCenter();
    })
});