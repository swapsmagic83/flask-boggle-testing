
let submitBtn= document.querySelector('.btn')
 inputText = document.querySelector('#input')
wordlist=document.querySelector('.wordlist')
msg= document.querySelector('.msg')
scorediv = document.querySelector('#score')
score=0
correctwords=[]
let bestscore =  JSON.parse(localStorage.getItem('bestscore')) || null
bestScorediv=document.querySelector('#best-score')
bestScorediv.innerText = `Your Best Score: ${bestscore}`
submitBtn.disabled = false
time = 60
timerdiv = document.querySelector('#timer')
let count = JSON.parse(localStorage.getItem('count')) || 0

clickEventFunc = function(e){
    e.preventDefault()
    
    let text = inputText.value
    // Post method to call API via axios
    let responsePromise = axios({
        url: 'http://127.0.0.1:5000/find-word?input=' + text,
        method: "GET"
      })
    responsePromise.then((response) => {
        if(response.data.result == 'not-word'){
            msg.innerText = `${text} is `+ response.data.result   
        }
        else if( response.data.result == 'not-on-board'){
            msg.innerText = `${text} is `+ response.data.result    
        }
        else if(response.data.result == 'ok' && !correctwords.includes(text)){
            correctwords.push(text)
            msg.innerText = `${text} is `+ response.data.result
           
            score = score + text.length
            scorediv.innerText=`Score: ${score}`
            li=document.createElement('li')
            li.innerText= text
            wordlist.append(li)
            if(bestscore==null){
                bestscore = score
                localStorage.setItem('bestscore', JSON.stringify(bestscore))
            }
            else if(score > bestscore){
                bestscore =  score
                localStorage.setItem('bestscore', JSON.stringify(bestscore))
            }
        }
        
    })   
    inputText.value=''
}
submitBtn.addEventListener('click', clickEventFunc)
interval = setInterval(function(){
        
        time--
        if(time == 0){
            count++
            clearInterval(interval)
            submitBtn.disabled = true
           localStorage.setItem('count',JSON.stringify(count))
           let scoreResponse = axios({
            url: 'http://127.0.0.1:5000/send-score',
            method: "POST",
            data:{
                'bestscore':bestscore,
                'count':count
            }
        })
        scoreResponse.then((response)=>{
            
            if(response.request.status != 200){
                alert('unable to send info to server')
            }
        })
        }
        timerdiv.innerText = `Time left: ${time} secs`
    },1000)






