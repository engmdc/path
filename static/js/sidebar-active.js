// Highlight active sidebar item based on current URL
document.addEventListener('DOMContentLoaded', function() {
    // Get current URL path
    const currentPath = window.location.pathname;
    
    // Find all sidebar links
    const sidebarLinks = document.querySelectorAll('.sidebar .nav-link');
    
    // Check each link against current path
    sidebarLinks.forEach(link => {
        const href = link.getAttribute('href');
        
        // Skip '#' links
        if (href === '#') return;
        
        // Check if the current path starts with the link's href (for nested routes)
        // or if they are exactly the same
        if (href && (currentPath === href || 
                    (href !== '/' && currentPath.startsWith(href)) ||
                    (currentPath.includes(href) && href.length > 1))) {
            
            // Add active class to the link
            link.classList.add('active');
            
            // If link is in a submenu, expand the parent menu
            const parentCollapse = link.closest('.multi-level');
            if (parentCollapse) {
                parentCollapse.classList.add('show');
                
                // Also highlight the parent menu item
                const parentLink = document.querySelector(`[data-bs-target="#${parentCollapse.id}"]`);
                if (parentLink) {
                    parentLink.classList.add('active');
                    parentLink.setAttribute('aria-expanded', 'true');
                }
            }
        }
    });
});
