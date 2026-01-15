// Initialize map
const map = L.map("leaflet-map").setView([45.55, -73.66], 11);

// Base layer
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap"
}).addTo(map);

// Cluster group
const clusters = L.markerClusterGroup({
  chunkedLoading: true
});

map.addLayer(clusters);

// Fetch + update markers
function applyFilters() {
  const form = document.getElementById("filter-form");
  const params = new URLSearchParams(new FormData(form));

  fetch(`/filter_map?${params.toString()}`)
    .then(res => res.json())
    .then(data => {
      clusters.clearLayers();

      data.forEach(row => {
        const date = new Date(row.DATE).toISOString().split("T")[0]; // YYYY-MM-DD format of incident date 
        const marker = L.marker([row.LATITUDE, row.LONGITUDE]).bindPopup(`${date}`);
        clusters.addLayer(marker);
      });
    });
}
