document.querySelector('#year').innerHTML = new Date().getFullYear();
const breakfast_link = document.querySelector('#breakfast-link');
const lunch_link = document.querySelector('#lunch-link');
const dinner_link = document.querySelector('#dinner-link');
const drinks_link = document.querySelector('#drinks-link');
const desserts_link = document.querySelector('#desserts-link');
const breakfast = document.querySelector('#breakfast');
const lunch = document.querySelector('#lunch');
const dinner = document.querySelector('#dinner');
const drinks = document.querySelector('#drinks');
const desserts = document.querySelector('#desserts');
breakfast_link.addEventListener('click', ()=>{
  breakfast.style.display = 'block';
  lunch.style.display = 'none';
  dinner.style.display = 'none';
  drinks.style.display = 'none';
  desserts.style.display = 'none';
})
lunch_link.addEventListener('click', ()=>{
  breakfast.style.display = 'none';
  lunch.style.display = 'block';
  dinner.style.display = 'none';
  drinks.style.display = 'none';
  desserts.style.display = 'none';
})
dinner_link.addEventListener('click', ()=>{
  breakfast.style.display = 'none';
  lunch.style.display = 'none';
  dinner.style.display = 'block';
  drinks.style.display = 'none';
  desserts.style.display = 'none';
})
drinks_link.addEventListener('click', ()=>{
  breakfast.style.display = 'none';
  lunch.style.display = 'none';
  dinner.style.display = 'none';
  drinks.style.display = 'block';
  desserts.style.display = 'none';
})
desserts_link.addEventListener('click', ()=>{
  breakfast.style.display = 'none';
  lunch.style.display = 'none';
  dinner.style.display = 'none';
  drinks.style.display = 'none';
  desserts.style.display = 'block';
})