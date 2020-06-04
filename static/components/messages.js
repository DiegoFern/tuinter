
var app = new Vue({
  el: '#app',

  data() {
    return {

    'user':'',
    'messages':[1,2,3],
    'new':'',
    'newMsg':''
    }
  },
  mounted(){
    axios.get('/list_message').then(res=>{
          this.user = res.data.user
          this.messages = res.data.messages
          console.log(res.data.messages)
          }
      )
  },
  methods:{
    send_msg(){
      if (this.newMsg!='')
          {axios.post('/list_message',{'message':this.newMsg}).then( (res,data)=>{
                if (!res.error){
                  this.messages.push(this.newMsg,()=>{ this.newMsg='' })
                }else{console.log(res)}

          })
    }}

  }

  })


