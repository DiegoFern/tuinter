app = new Vue({
  el:'#app',
  data(){
    return {
    'follows':[],
     'propolsal':[]
      }
    },
  methods:{
    f(m){
      alert(m)}
  },
  mounted(){
    axios.get('/api_follow').then(res=>{
        this.follows = res.data.follows;
        this.propolsal = res.data.propolsal;
        this.user =res.data.user}
    )
    }

  })
