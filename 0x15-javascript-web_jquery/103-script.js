(function ($) {
  'use strict';

  function fetchAndDisplayTranslation() {
    const languageCode = $('#language_code').val();

    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $(document).ready(function () {
    $('#btn_translate').click(function () {
      fetchAndDisplayTranslation();
    });

    $('#language_code').keypress(function (event) {
      if (event.keyCode === 13) {
        fetchAndDisplayTranslation();
      }
    });
  });

})(jQuery);
