import { Component, OnInit } from '@angular/core';
import { Publication_Topics } from 'src/app/interfaces/publication_topics';
import { TopicsService } from 'src/app/services/topics.service';

@Component({
  selector: 'app-manage-topics',
  templateUrl: './manage-topics.component.html',
  styleUrls: ['./manage-topics.component.css']
})
export class ManageTopicsComponent implements OnInit {

  public topics!: Publication_Topics[];
  public topicAdded!: string;           // description of the topic to be added

  constructor(private topicsService: TopicsService) { }

  ngOnInit(): void {

    this.getTopics();

  }

  getTopics() {
    return this.topicsService.getTopics().subscribe((topics) => {
      console.log("topics")
      console.log(topics)
      this.topics = topics;
    })
  }

  createTopic(description: string) {
    return this.topicsService.createTopic(description);
  }

}
