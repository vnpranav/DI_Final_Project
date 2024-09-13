$(document).ready( function () {
   $('.increment-btn').click(function(e){
      e.preventDefault()

      var inc_value = $(this).closest('.product_data').find('.qty-input').val();
      var current_val = parseInt(inc_value, 10);
      if (isNaN(current_val)) {
         current_val = 0;
      }

      if (current_val < 10){
         current_val++;
         $(this).closest('.product_data').find('.qty-input').val(current_val);
      }
   })

   $('.decrement-btn').click(function(e){
      e.preventDefault()

      var dec_value = $(this).closest('.product_data').find('.qty-input').val();
      var current_val = parseInt(dec_value, 10);
      if (isNaN(current_val)) {
         current_val = 0;
      }

      if (current_val > 1){
         current_val--;
         $(this).closest('.product_data').find('.qty-input').val(current_val);
      }
   })


   $('.addToCartBtn').click(function (e) {
      e.preventDefault()

      var prod_id = $(this).closest('.product_data').find('.prod_id').val();
      var prod_qty = $(this).closest('.product_data').find('.qty-input').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();

      $.ajax({
         method: "POST",
         url: "/add-to-cart/",
         data: {
            'prod_id': prod_id,
            'prod_qty': prod_qty,
            csrfmiddlewaretoken : token
         },
         success: function (response) {
            console.log(response);
            alertify.success(response.status)
         },
         error: function (response) {
            console.log(response);
            alertify.error("Error adding product to cart");
        }
      })
   })

   $('.addToWishlist').click(function (e) {
      e.preventDefault()

      var prod_id = $(this).closest('.product_data').find('.prod_id').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();

      $.ajax({
         method: "POST",
         url: "/add-to-wishlist/",
         data: {
            'prod_id': prod_id,
            csrfmiddlewaretoken : token
         },
         success: function (response) {
            console.log(response);
            alertify.success(response.status)
         },
         error: function (response) {
            console.log(response);
            alertify.error("Error adding product to wishlist");
        }
      })
   })

   $('.changeQty').click(function (e) {
      e.preventDefault()

      var prod_id = $(this).closest('.product_data').find('.prod_id').val();
      var prod_qty = $(this).closest('.product_data').find('.qty-input').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();

      $.ajax({
         method: "POST",
         url: "/update-cart/",
         data: {
            'prod_id': prod_id,
            'prod_qty': prod_qty,
            csrfmiddlewaretoken : token
         },
         success: function (response) {
            console.log(response);
            alertify.success(response.status)
         },
         error: function (response) {
            console.log(response);
            alertify.error("Error updating product to cart");
        }
      })
   })

   $('.removecart').click(function(e){
      e.preventDefault()
      var prod_id = $(this).closest('.product_data').find('.prod_id').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();

      $.ajax({
         method: "POST",
         url: "/removecart/",
         data: {
            'prod_id': prod_id,
            csrfmiddlewaretoken : token
         },
         success: function (response) {
            console.log(response);
            alertify.success(response.status)
            location.reload()
         },
         error: function (response) {
            console.log(response);
            alertify.error("Error removing product from cart");
         }
      })
   })

   $('.removewishlist').click(function(e){
      e.preventDefault()
      var prod_id = $(this).closest('.product_data').find('.prod_id').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();

      $.ajax({
         method: "POST",
         url: "/removewishlist/",
         data: {
            'prod_id': prod_id,
            csrfmiddlewaretoken : token
         },
         success: function (response) {
            console.log(response);
            alertify.success(response.status)
            location.reload()
         },
         error: function (response) {
            console.log(response);
            alertify.error("Error removing product from wishlist");
         }
      })
   })
})