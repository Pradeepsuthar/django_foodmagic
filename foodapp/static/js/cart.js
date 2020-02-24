// ************************************************
// Shopping Cart API
// ************************************************

var shoppingCart = (function() {
    // =============================
    // Private methods and propeties
    // =============================
    cart = [];
    
    // Constructor
    function Item(name, price, count) {
      this.name = name;
      this.price = price;
      this.count = count;
    }
    
    // Save cart
    function saveCart() {
      localStorage.setItem('shoppingCart', JSON.stringify(cart));
    }
    
      // Load cart
    function loadCart() {
      cart = JSON.parse(localStorage.getItem('shoppingCart'));
    }
    if (localStorage.getItem("shoppingCart") != null) {
      loadCart();
    }
    
  
    // =============================
    // Public methods and propeties
    // =============================
    var obj = {};
    
    // Add to cart
    obj.addItemToCart = function(name, price, count) {
      for(var item in cart) {
        if(cart[item].name === name) {
          cart[item].count ++;
          saveCart();
          return;
        }
      }
      var item = new Item(name, price, count);
      cart.push(item);
      saveCart();
    }
    // Set count from item
    obj.setCountForItem = function(name, count) {
      for(var i in cart) {
        if (cart[i].name === name) {
          cart[i].count = count;
          break;
        }
      }
    };
    // Remove item from cart
    obj.removeItemFromCart = function(name) {
        for(var item in cart) {
          if(cart[item].name === name) {
            cart[item].count --;
            if(cart[item].count === 0) {
              cart.splice(item, 1);
            }
            break;
          }
      }
      saveCart();
    }
  
    // Remove all items from cart
    obj.removeItemFromCartAll = function(name) {
      for(var item in cart) {
        if(cart[item].name === name) {
          cart.splice(item, 1);
          break;
        }
      }
      saveCart();
    }
  
    // Clear cart
    obj.clearCart = function() {
      cart = [];
      saveCart();
    }
  
    // Count cart 
    obj.totalCount = function() {
      var totalCount = 0;
      for(var item in cart) {
        totalCount += cart[item].count;
      }
      return totalCount;
    }
  
    // Total cart
    obj.totalCart = function() {
      var totalCart = 0;
      for(var item in cart) {
        totalCart += cart[item].price * cart[item].count;
      }
      return Number(totalCart.toFixed(2));
    }
  
    // List cart
    obj.listCart = function() {
      var cartCopy = [];
      for(i in cart) {
        item = cart[i];
        itemCopy = {};
        for(p in item) {
          itemCopy[p] = item[p];
        }
        itemCopy.total = Number(item.price * item.count).toFixed(2);
        cartCopy.push(itemCopy)
      }
      return cartCopy;
    }
  
    // cart : Array
    // Item : Object/Class
    // addItemToCart : Function
    // removeItemFromCart : Function
    // removeItemFromCartAll : Function
    // clearCart : Function
    // countCart : Function
    // totalCart : Function
    // listCart : Function
    // saveCart : Function
    // loadCart : Function
    return obj;
  })();
  
  
  // *****************************************
  // Triggers / Events
  // ***************************************** 
  // Add item
  $('.add-to-cart').click(function(event) {
    event.preventDefault();
    var name = $(this).data('name');
    var price = Number($(this).data('price'));
    shoppingCart.addItemToCart(name, price, 1);
    displayCart();
  });
  
  // Clear items
  $('.clear-cart').click(function() {
    shoppingCart.clearCart();
    displayCart();
  });
  
  
  function displayCart() {
    var cartArray = shoppingCart.listCart();
    var output = "";
    for(var i in cartArray) {
            output+= `
                    <li class="list-group-item d-flex justify-content-between lh-condensed border rounded-0">
                      <div>
                        <h6 class="my-0">${cartArray[i].name} (${cartArray[i].count})</h6>
                        <small class="text-muted"><a href="#" class="delete-item text-decoration-none text-danger" data-name="${cartArray[i].name}">Delete</a></small>
                       
                        <nav aria-label="..." class="my-1">
                          <ul class="pagination pagination-sm">
                            <li class="page-item"><a class="page-link minus-item" href="#" data-name="${cartArray[i].name}">-</a></li>
                            <li class="page-item"><a class="page-link" href="#">${cartArray[i].count}</a></li>
                            <li class="page-item"><a class="page-link plus-item" href="#" data-name="${cartArray[i].name}">+</a></li>
                          </ul>
                        </nav>
                      </div>
                      <span class="text-muted">₹${cartArray[i].price}</span>
                    </li>`;
    }
    $('.show-cart').html(output);
    $('.total-cart').html(shoppingCart.totalCart());
    $('.total-count').html(shoppingCart.totalCount());
  }
  
  // Delete item button
  
  $('.show-cart').on("click", ".delete-item", function(event) {
    var name = $(this).data('name')
    shoppingCart.removeItemFromCartAll(name);
    displayCart();
  })
  
  
  // -1
  $('.show-cart').on("click", ".minus-item", function(event) {
    var name = $(this).data('name')
    shoppingCart.removeItemFromCart(name);
    displayCart();
  })
  // +1
  $('.show-cart').on("click", ".plus-item", function(event) {
    var name = $(this).data('name')
    shoppingCart.addItemToCart(name);
    displayCart();
  })
  
  // Item count input
  $('.show-cart').on("change", ".item-count", function(event) {
     var name = $(this).data('name');
     var count = Number($(this).val());
    shoppingCart.setCountForItem(name, count);
    displayCart();
  });
  
  displayCart();
  


