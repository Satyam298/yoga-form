function formValidation(age, contact_number){
    if(age<18 || age>65) {
        alert('Age must be between 18 and 65');
        return false;
    }
    var phoneno = /^\d{10}$/;
    if (contact_number.match(phoneno)){
        return true;
    }
    else{
        alert("Invalid Contact Number!");
        return false;
    }
    return true;
}
document.getElementById("formdata").addEventListener("submit",function(e){
    e.preventDefault();
        first_name=document.getElementById("first_name").value;
        last_name=document.getElementById("last_name").value;
        age=document.getElementById("age").value;
        email=document.getElementById("email").value;
        contact_number=document.getElementById("contact_number").value;
        if (document.getElementById('g1').checked) {
            gender = document.getElementById('g1').value;
        }
        if (document.getElementById('g2').checked) {
            gender = document.getElementById('g2').value;
        } 
        batch_id=document.getElementById("batch_id").value;
        amount=500;
        payment_successful="True";
    if(formValidation(age,contact_number)==true){
        const formData=new FormData();
        formData.append('first_name',first_name);
        formData.append('last_name',last_name);
        formData.append('age',age);
        formData.append('email',email);
        formData.append('contact_number',contact_number);
        formData.append('gender',gender);
        formData.append('batch_id',batch_id);
        formData.append('amount',amount);
        formData.append('payment_successful',payment_successful);
        console.log(formData);
        
        fetch('yoga-form-production.up.railway.app',{
            method:'POST',
            body:formData,
        })
        .then(response=>response.json())
        .then(response => console.log(JSON.stringify(response)))
        .then(data=>{
            console.log('Success:',data);
            alert("Yay ! " + first_name +  "\n\nYour details have been registered successfully\n\nYou will receive an email with payment link.\n\nKindly do the payment within 1 month to comfirm your admission.")
            document.getElementById("first_name").value = "";
            document.getElementById("last_name").value="";
            document.getElementById("age").value="";
            document.getElementById("email").value = "";
            document.getElementById("contact_number").value = "";
            document.getElementById("g1").checked = false;
            document.getElementById("g2").checked = false;
            document.getElementById("output-message").innerText = "Your details have been successfully registered!"
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
            alert("Oops! Error saving your details. Please try again!\n\nEmail Address and Contact Number must be unique!");
            document.getElementById("output-message").innerText = "Oops! Error saving your details. Please try again!"
            setTimeout(function(){ 
            document.getElementById("output-message").style.display = "none";
            }, 3000);
            setTimeout(function(){ 
            document.getElementById("output-message").style.display = "";
            }, 1000);
        })
    }
});