// Populating a table with basic jQuery because it's nicer than hardcoding html
var links = [
  {
    name: 'Roam',
    description: "Thinkin'",
    linkHref: 'https://roamresearch.com/#/app/tuck',
    imgSrc: 'https://preview.redd.it/ctvemkioy7741.png?width=428&format=png&auto=webp&s=b685204aa024e3665d0abb3cf42145494e975375',
    imgHeight: '40px',
  },
  {
    name: 'Twitter',
    description: "Yakkin'",
    linkHref: 'https://twitter.com/ryntck',
    imgSrc: 'https://image.flaticon.com/icons/png/512/23/23931.png',
    imgHeight: '40px',
  },
  {
    name: 'GitHub',
    description: "Hackin'",
    linkHref: 'https://github.com/ryantuck',
    imgSrc: "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    imgHeight: '50px',
  },
  {
    name: 'Stack Overflow',
    description: "Askin'",
    linkHref: 'https://stackoverflow.com/users/1700270/ryantuck',
    imgSrc: "https://www.shareicon.net/data/2048x2048/2015/08/10/82808_stackoverflow_4096x4096.png",
    imgHeight: '50px',
  },
]

var linksUl = $('#links');
for (i = 0; i < links.length; i++) {
  link = links[i];

  // react would be way cleaner

  linksUl.append($('<li>')
    .append($('<div>').attr('class', 'linkDiv')
      .append($('<span>')
        .append($('<a>')
          .attr('target', '_blank')
          .attr('href', link.linkHref)
          .text(link.description)
        )
      )
      .append($('<div>').attr('class', 'linkImgDiv').append($('<img>')
        .attr('src', link.imgSrc)
        // this is gross
        .attr('style', 'height: ' + link.imgHeight)
        .text(link.name)
      ))
    )
  )
}