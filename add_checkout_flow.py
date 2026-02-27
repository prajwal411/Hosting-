#!/usr/bin/env python3
"""Add checkout modal and Razorpay integration to the website"""

file_path = "c:\\Users\\abhis\\Documents\\Abhishek_Documents\\websites\\vercelhost\\index (1).html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Modal HTML and JavaScript to inject before </body>
modal_code = '''<!-- Checkout Modal -->
<div id="checkoutModal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:9999;justify-content:center;align-items:center;flex-direction:column;">
  <div style="background:white;border-radius:12px;padding:40px;max-width:500px;width:90%;box-shadow:0 10px 40px rgba(0,0,0,0.2);">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;">
      <h3 style="margin:0;font-size:24px;font-weight:600;">Complete Your Order</h3>
      <button onclick="closeCheckoutModal()" style="background:none;border:none;font-size:28px;cursor:pointer;color:#999;">&times;</button>
    </div>
    
    <form id="checkoutForm" onsubmit="handleCheckoutSubmit(event)">
      <div style="margin-bottom:20px;">
        <label for="email" style="display:block;margin-bottom:8px;font-weight:500;">Email Address*</label>
        <input type="email" id="email" name="email" required style="width:100%;padding:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;" placeholder="your@email.com">
        <p style="font-size:12px;color:#666;margin-top:4px;">Where you'll receive hosting setup details</p>
      </div>
      
      <div style="margin-bottom:24px;">
        <label for="domain" name="domain" style="display:block;margin-bottom:8px;font-weight:500;">Domain Name*</label>
        <input type="text" id="domain" name="domain" required style="width:100%;padding:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;" placeholder="example.com">
        <p style="font-size:12px;color:#666;margin-top:4px;">Your website domain</p>
      </div>
      
      <div style="background:#f8f9fa;padding:16px;border-radius:8px;margin-bottom:24px;">
        <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
          <span id="planNameDisplay" style="font-weight:500;">Starter Hosting</span>
          <span id="planPriceDisplay" style="font-weight:600;">₹8,260</span>
        </div>
        <p style="font-size:12px;color:#666;margin:0;">One-time setup fee (incl. GST)</p>
      </div>
      
      <button type="submit" style="width:100%;padding:14px;background:#1a1a1a;color:white;border:none;border-radius:8px;font-size:16px;font-weight:500;cursor:pointer;">Proceed to Payment</button>
    </form>
    
    <p style="text-align:center;font-size:12px;color:#999;margin-top:16px;margin-bottom:0;">Secure payment powered by Razorpay</p>
  </div>
</div>

<!-- Razorpay Script -->
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>

<script>
// Plan pricing data
const plans = {
  'starter': { name: 'Starter Hosting', amount: 826000, displayAmount: '₹8,260' }, // Amount in paise
  'business': { name: 'Business Hosting', amount: 2124000, displayAmount: '₹21,240' },
  'enterprise': { name: 'Enterprise Hosting', amount: 4130000, displayAmount: '₹41,300' }
};

let currentPlan = 'starter';

// Show checkout modal
function openCheckoutModal(planType = 'starter') {
  currentPlan = planType;
  document.getElementById('checkoutModal').style.display = 'flex';
  document.getElementById('planNameDisplay').textContent = plans[planType].name;
  document.getElementById('planPriceDisplay').textContent = plans[planType].displayAmount;
  document.getElementById('checkoutForm').reset();
}

// Close checkout modal
function closeCheckoutModal() {
  document.getElementById('checkoutModal').style.display = 'none';
  document.getElementById('checkoutForm').reset();
}

// Handle checkout form submission
function handleCheckoutSubmit(event) {
  event.preventDefault();
  
  const email = document.getElementById('email').value;
  const domain = document.getElementById('domain').value;
  const plan = plans[currentPlan];
  
  // Validate inputs
  if (!email || !domain) {
    alert('Please fill in all fields');
    return;
  }
  
  // Initiate Razorpay payment
  const options = {
    key: 'razorpay_live_YourKeyHere', // Replace with your Razorpay key
    amount: plan.amount, // Amount in paise (₹8260 = 826000 paise)
    currency: 'INR',
    name: 'CloudMeld Hosting',
    description: plan.name,
    image: 'https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/683044c014cce5c138736553_9e64493c28652d3ea3d936494ab72d3d_logo_dark.svg',
    prefill: {
      email: email,
      contact: ''
    },
    notes: {
      domain: domain,
      plan: currentPlan,
      planName: plan.name
    },
    handler: function(response) {
      // Payment successful
      console.log('Payment successful:', response);
      alert('Payment successful! We will setup your hosting for ' + domain + ' and send details to ' + email);
      
      // Here you can send the data to your backend
      // Example: sendPaymentDetails(email, domain, currentPlan, response.razorpay_payment_id);
      
      closeCheckoutModal();
    },
    modal: {
      ondismiss: function() {
        console.log('Payment modal closed');
      }
    }
  };
  
  const rzp = new Razorpay(options);
  rzp.open();
}

// Close modal when clicking outside
document.addEventListener('DOMContentLoaded', function() {
  const modal = document.getElementById('checkoutModal');
  modal.addEventListener('click', function(event) {
    if (event.target === modal) {
      closeCheckoutModal();
    }
  });
  
  // Attach click handlers to all "Get Started" buttons
  const getStartedButtons = document.querySelectorAll('a[href="#contact"], button:contains("Get Started")');
  
  // More specific targeting for the Get Started buttons in pricing section
  const allButtons = document.querySelectorAll('.button');
  allButtons.forEach(button => {
    if (button.textContent.includes('Get Started') || button.textContent.includes('Choose Plan') || button.textContent.includes('Talk to Sales')) {
      button.style.cursor = 'pointer';
      
      // Determine plan type from button context
      let planType = 'starter';
      if (button.textContent.includes('Choose Plan')) {
        planType = 'business';
      } else if (button.textContent.includes('Talk to Sales')) {
        planType = 'enterprise';
      }
      
      button.onclick = function(e) {
        if (button.getAttribute('href') === '#contact') {
          e.preventDefault();
          openCheckoutModal(planType);
        }
      };
    }
  });
});

// Optional: Handle escape key to close modal
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeCheckoutModal();
  }
});
</script>

<style>
#checkoutModal {
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

#checkoutForm input {
  transition: border-color 0.2s;
}

#checkoutForm input:focus {
  outline: none;
  border-color: #7bb07f;
  box-shadow: 0 0 0 3px rgba(123, 176, 127, 0.1);
}

#checkoutForm button:hover {
  background: #0f0f0f;
}
</style>'''

# Find the closing body tag and insert the modal code
if '</body>' in content:
    content = content.replace('</body>', modal_code + '\n</body>')
    
    # Save the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Checkout modal and Razorpay integration added successfully!")
    print("\n📝 Configuration Steps:")
    print("1. Replace 'razorpay_live_YourKeyHere' with your actual Razorpay API key")
    print("2. To get your Razorpay key:")
    print("   - Visit https://dashboard.razorpay.com/")
    print("   - Login or sign up for an account")
    print("   - Go to Settings > API Keys")
    print("   - Copy your Key ID (live or test key)")
    print("\n🎯 How it works:")
    print("- Click 'Get Started' button → Form opens")
    print("- Enter email and domain name")
    print("- Click 'Proceed to Payment'")
    print("- Razorpay payment gateway opens")
    print("- After successful payment, user sees confirmation")
    print("\n💡 Features:")
    print("✓ Modal form for email and domain collection")
    print("✓ Razorpay payment integration")
    print("✓ Auto-detect plan type from button")
    print("✓ Close modal with X button or Escape key")
    print("✓ Responsive design")
    
else:
    print("❌ Could not find closing body tag")
