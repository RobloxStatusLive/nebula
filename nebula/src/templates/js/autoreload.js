// Copyright 2022 iiPython

// Initialization
const LocaleFormatter = new Intl.DateTimeFormat("en-US", { hour12: true, hour: "2-digit", minute: "2-digit" });
const DateTimeFormatter = new Intl.DateTimeFormat("en-US", { month: "2-digit", day: "2-digit", year: "2-digit" });

$("[data-bs-toggle='tooltip']").each((i, e) => { new bootstrap.Tooltip(e); })

// Handle historical data
var historyChart = null;
let formatDate = (date = new Date()) => DateTimeFormatter.format(new Date(date)).replace(/\//g, "-");
function hsRenderDate(date) {
    let serviceID = $("#hscanvas").attr("data-rsl-id");

    // Create the chart
    $.get(`/api/day/${formatDate(date)}/${serviceID}`, {}, (r) => {
        const ctx = document.getElementById("hscanvas").getContext("2d");
        if (historyChart) historyChart.destroy();
        historyChart = new Chart(ctx, {
            type: "line",
            options: {
                responsive: false,
                maintainAspectRatio: false,
                scales: {
                    x: { title: { display: true, text: "Time" } },
                    y: { title: { display: true, text: "Ping" }, ticks: { callback: (v) => { return `${v}ms` } } }
                }
            }
        });
        historyChart.data.datasets = [{
            label: "Ping",
            data: Object.entries(r.data).filter(entry => entry[0] % 5 === 0).map(v => { return { x: LocaleFormatter.format(v[0]), y: v[1].ping } } ),
            borderColor: "rgb(159, 159, 159)"
        }];
        historyChart.update();
    })
}
function hsRenderCustomDate() {
    bootbox.prompt({
        title: "Select date to view",
        inputType: "date",
        callback: hsRenderDate
    });
}
$(NebulaConfig.clickElement).click((e) => {
    let serviceID = $(e.currentTarget).parent().attr("data-rsl-id");
    bootbox.dialog({
        title: $(NebulaConfig.clickElement.replace("data-rsl-id", `data-rsl-id='${serviceID}'`)).text(),
        message: `
        <div><canvas id = "hscanvas" height = "450" width = "600" data-rsl-id = "${serviceID}"></canvas></div>
        <p class = "modal-notice"><a onclick = "hsRenderDate();">Today</a> · <a onclick = "hsRenderCustomDate();">Custom</a></p>
        `,
        buttons: { ok: { label: "Close", className: "btn btn-secondary", callback: () => {} } },
        onEscape: true
    })
    hsRenderDate();
})

// Handle autoreloading
setInterval(() => {
    $.get("/api/status", {}, (d) => {

        // Load status information
        $("nav").css("background-image", `url("/s/img/${d.status}.png")`);

        // Render our service data
        for (let service of Object.values(d.data)) {
            let elems = $(NebulaConfig.clickElement.replace("data-rsl-id", `data-rsl-id='${service.id}'`)).children();
            let color = { up: "green", slow: "yellow", down: "red" }[service.guess.name];

            // Update service data
            if (NebulaConfig.elementOverwriteCallback) NebulaConfig.elementOverwriteCallback(elems);
            else {
                $(elems[0]).css("color", `var(--ii-${color})`);  // Service header
                $(elems[1]).text(`${Math.round(service.ping)}ms`);  // Ping time
                $(elems[2]).text(service.guess.reason);  // Guess element (.card-text)
            }
        }
    })
}, 60000);  // 1m since our internal database doesn't update faster than that
