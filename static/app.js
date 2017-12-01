function changeHeight() {
    var maxHeight2 = -1;

    $('.overzoom').each(function () {
        maxHeight2 = maxHeight2 > $(this).height() ? maxHeight2 : $(this).height();
    });

    $('.overzoom').each(function () {
        $(this).height(maxHeight2);
    });

}

$(document).scroll(function () {

        var maxHeight = $(document).height();
        var currentScroll = $(window).scrollTop() + $(window).height();


        if (maxHeight <= currentScroll + 400) {
            if (mode == 0) {
                if (typeof arr[i] != "undefined") {
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
                    if (typeof gif[i] != "undefined") {
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m] + '" download><img src="../static/images/' + gif[m] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 1] + '" download><img src="../static/images/' + gif[m + 1] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 2] + '" download><img src="../static/images/' + gif[m + 2] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 3] + '" download><img src="../static/images/' + gif[m + 3] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 4] + '" download><img src="../static/images/' + gif[m + 4] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 5] + '" download><img src="../static/images/' + gif[m + 5] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 6] + '" download><img src="../static/images/' + gif[m + 6] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 7] + '" download><img src="../static/images/' + gif[m + 7] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 8] + '" download><img src="../static/images/' + gif[m + 8] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 9] + '" download><img src="../static/images/' + gif[m + 9] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 10] + '" download><img src="../static/images/' + gif[m + 10] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[m + 11] + '" download><img src="../static/images/' + gif[m + 11] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);

                        m += 12;
                    }
                }
            }
        }

        changeHeight();
        $('img').flexVerticalCenter();

    }
);