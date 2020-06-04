Vue.component('card',{
  props : ['m','click','nam'],
  template:`
  <div class=card >
        {{ m['name'] }} <BR/>
        {{ m['email']}}
        <button v-if=click v-on:click='click(m)'>{{ nam }}</button>
  </div>
  `
})

