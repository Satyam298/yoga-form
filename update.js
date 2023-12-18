document.getElementById("formdata").addEventListener("submit",function(e){
    e.preventDefault();
        email=document.getElementById("email").value;
        batch_id=document.getElementById("batch_id").value;
        amount=500;
        payment_successful="True";
        const formData=new FormData();
        formData.append('email',email);
        formData.append('batch_id',batch_id);
        formData.append('amount',amount);
        formData.append('payment_successful',payment_successful);
        console.log(formData);

        fetch('yoga-form-production.up.railway.app/update',{
            method:'POST',
            body:formData,
        })
        .then(response=>response.json())
        .then(data=>{
            console.log('Success:',data);
            alert("Yay ! Your details have been updated successfully\n\nYou will receive an email with payment link.\n\nKindly do the payment within 1 month to comfirm your admission.")

            document.getElementById("email").value = "";
        
            document.getElementById("output-message").innerText = "Your details have been successfully updated!"
            setTimeout(function(){ 
                document.getElementById("output-message").style.display = "none";
                 }, 3000);
                setTimeout(function(){ 
                document.getElementById("output-message").style.display = "";
                 }, 1000);
        })
        .catch(error=>{
            console.log('Error:',error);
            console.error('Error:', error);
            alert("Oops! Error saving your details. Please try again!\n\nYou might not be registered!");
            document.getElementById("output-message").innerText = "Oops! Error saving your details. Please try again!\nYou might not be registered"
            setTimeout(function(){ 
            document.getElementById("output-message").style.display = "none";
            }, 3000);
            setTimeout(function(){ 
            document.getElementById("output-message").style.display = "";
            }, 1000);
        })
});