import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Observable } from 'rxjs';
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
  topicForm !: FormGroup;

  constructor(private topicsService: TopicsService, private fb: FormBuilder) { }

  ngOnInit(): void {

    this.getTopics();
    this.topicForm = this.fb.group({
      description: [null]
    });

  }

  getTopics() {
    return this.topicsService.getTopics().subscribe((topics) => {
      this.topics = topics;
    })
  }

  topicSubmit() {
    return this.topicsService.createTopic(this.topicForm).subscribe((topic) => {
      this.topicAdded = topic;
      this.getTopics();
      this.topicForm.reset();
    });
  }

  update() {
    this.getTopics();
  }


}
