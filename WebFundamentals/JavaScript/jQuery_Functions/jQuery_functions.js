<script>
  $(document).ready(function() {
    $(#hide).click(function(){
      $(#hideshow).hide();
    });

    $(#show).click(function(){
      $(#hideshow).show();
    });

    $(#toggle).click(function(){
      $(#hideshow).toggle();
    });

    $(#slideup).click(function(){
      $(#slide).slideUp();
    });

    $(#slidedown).click(function(){
      $(#slide).slideDown();
    });

    $(#slidetoggle).click(function(){
      $(#slide).slideToggle();
    });

    $(#fadein).click(function(){
      $(#fade).fadeIn();
    });

    $(#fadeout).click(function(){
      $(#fade).fadeOut();
    });

    $(#addclass).click(function(){
      $(#add).addclass(.blue);
    });

    $(#before).click(function(){
      $(#baa).before(<p>Test</p>);
    });

    $(#after).click(function(){
      $(#baa).after(<p>Test</p>);
    });

    $(#append).click(function(){
      $(#baa).append(<p>Test</p>);
    });

    $(#addHTML).click(function(){
      $(#html).addHTML();
    });

    $(#att).click(function(){
      $(#attribute).attribute();
    });

    $(#val).click(function(){
      $(#value).val();
    });

  }

</script>
