document.querySelector('#year').innerHTML = new Date().getFullYear();
const options = {
  threshold: 0.4,
}
 const fade = new IntersectionObserver((entries, fade)=>{
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.remove('fade')
      entry.target.classList.add('fade-in')
    }
    else{
      entry.target.classList.add('fade')
      entry.target.classList.remove('fade-in')
    }
  })
}, options)
document.querySelectorAll('.menu-card').forEach(item=>{
  fade.observe(item)
})



