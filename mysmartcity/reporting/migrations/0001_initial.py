from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='IssueReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(choices=[('water', 'Water Leak'), ('electricity', 'Electricity Fault'), ('pothole', 'Pothole'), ('waste', 'Waste Collection')], max_length=20)),
                ('description', models.TextField()),
                ('location', models.CharField(blank=True, default='', max_length=255)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='issue_photos/')),
                ('voice_note', models.FileField(blank=True, null=True, upload_to='voice_notes/')),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('rejected', 'Rejected')], default='submitted', max_length=20)),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['-submitted_at']},
        ),
    ]