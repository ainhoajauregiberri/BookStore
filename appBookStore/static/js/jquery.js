jQuery.fx.prototype = {

// Simple 'show' function
show: function(){
    // Remember where we started, so that we can go back to it later
    this.options.orig[this.prop] = jQuery.attr( this.elem.style, this.prop );
    this.options.show = true;

    // Begin the animation
    // Make sure that we start at a small width/height to avoid any
    // flash of content
    this.custom(this.prop == "width" || this.prop == "height" ? 1 : 0, this.cur());

    // Start by showing the element
    jQuery(this.elem).show();
},

// Simple 'hide' function
hide: function(){
    // Remember where we started, so that we can go back to it later
    this.options.orig[this.prop] = jQuery.attr( this.elem.style, this.prop );
    this.options.hide = true;

    // Begin the animation
    this.custom(this.cur(), 0);
},

};