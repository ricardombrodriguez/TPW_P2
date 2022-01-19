import { Component, OnInit } from '@angular/core';
import { Publication } from 'src/app/interfaces/publication';
import { PublicationService } from 'src/app/services/publication.service';

@Component({
  selector: 'app-pendent-publications',
  templateUrl: './pendent-publications.component.html',
  styleUrls: ['./pendent-publications.component.css']
})
export class PendentPublicationsComponent implements OnInit {

  public publications!: Publication[];

  constructor(private publicationsService: PublicationService) { }

  ngOnInit(): void {

    this.getPendentPublications();

  }

  getPendentPublications(): void {
    this.publicationsService.getPendentPublications().subscribe((publications) => {
      this.publications = publications;
    });
  }


}
