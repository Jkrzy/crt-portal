# Generated by Django 2.2.4 on 2019-08-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0015_auto_20190821_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='contact_state',
            field=models.CharField(blank=True, choices=[('SD', 'South Dakota '), ('HI', 'Hawaii '), ('MD', 'Maryland '), ('VI', 'Virgin Islands '), ('CT', 'Connecticut '), ('IL', 'Illinois '), ('MP', 'Northern Mariana Islands '), ('AE', 'Armed Forces Canada '), ('IA', 'Iowa '), ('VA', 'Virginia '), ('AR', 'Arkansas '), ('AA', 'Armed Forces Americas '), ('MS', 'Mississippi '), ('AE', 'Armed Forces Europe '), ('WA', 'Washington '), ('KS', 'Kansas '), ('ME', 'Maine '), ('MO', 'Missouri '), ('NE', 'Nebraska '), ('OK', 'Oklahoma '), ('KY', 'Kentucky '), ('AL', 'Alabama '), ('NJ', 'New Jersey '), ('SC', 'South Carolina '), ('TN', 'Tennessee '), ('OR', 'Oregon '), ('ID', 'Idaho '), ('IN', 'Indiana '), ('TX', 'Texas '), ('VT', 'Vermont '), ('DC', 'District of Columbia '), ('RI', 'Rhode Island '), ('WI', 'Wisconsin '), ('MN', 'Minnesota '), ('AS', 'American Samoa '), ('AK', 'Alaska '), ('MA', 'Massachusetts '), ('GA', 'Georgia '), ('NM', 'New Mexico '), ('WY', 'Wyoming '), ('AE', 'Armed Forces Africa '), ('AE', 'Armed Forces Middle East '), ('NV', 'Nevada '), ('ND', 'North Dakota '), ('MI', 'Michigan '), ('DE', 'Delaware '), ('OH', 'Ohio '), ('LA', 'Louisiana '), ('PR', 'Puerto Rico '), ('GU', 'Guam '), ('CO', 'Colorado '), ('FL', 'Florida '), ('NH', 'New Hampshire '), ('NC', 'North Carolina '), ('MT', 'Montana '), ('PA', 'Pennsylvania '), ('CA', 'California '), ('UT', 'Utah '), ('AZ', 'Arizona '), ('WV', 'West Virginia '), ('AP', 'Armed Forces Pacific '), ('NY', 'New York ')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='employer_size',
            field=models.CharField(choices=[('15_or_more', '15 or more employees'), ('14_or_less', 'Fewer than 15 employees')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='how_many',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('not_sure', "I'm not sure"), ('yes', 'Yes')], default=None, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='place',
            field=models.CharField(choices=[('place_of_worship', 'Place of worship'), ('government_building', 'Another government building (courthouse, DMV, post office)'), ('workplace', 'Workplace or potential workplace'), ('healthcare', 'Healthcare facility (including mental health or long-term care)'), ('store', 'Retail/commercial building (store, restaurant, hotel, nightclub, theater, gym, or other commercial space)'), ('voting', 'Voting location or ballot (including mail-in ballots)'), ('incarcerated', 'Prison, jail, or juvenile corrections facility, or while otherwise incarcerated'), ('home,', 'Home, potential home, or services to help with purchasing a home (banks, lenders, or other financial services)'), ('public_space', 'Outdoor public space (including car, street, sidewalk, park)'), ('school', 'Educational institution (school, university), education program or educational activity (after school program or workshop)')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='primary_complaint',
            field=models.CharField(choices=[('fired', 'Fired, not hired, demoted, or asked to show more documentation than required'), ('prevented_from_service', 'Prevented from using a service or service terminated'), ('discriminated_against', 'Otherwise discriminated against'), ('retaliated', 'Retaliated against or otherwise mistreated for reporting an issue'), ('harassed', 'Harassed, threatened, assaulted, or otherwise made to feel unsafe (including sexual harassment or assault)'), ('vote', 'Ability to vote was impacted'), ('denied_housing', 'Denied housing or subjected to harmful living conditions'), ('denied_access', 'Denied access or removed from a location (including segregation)')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='public_or_private_employer',
            field=models.CharField(choices=[('private_employer', 'Private employer -- Businesses or non-profits not funded by the government such as retail stores, banks, or restaurants.'), ('not_sure', "I'm not sure"), ('public_employer', 'Public employer -- Funded by the government like a post office, fire department, courthouse, DMV, or public school. This could be at the local, state, or federal level.')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='public_or_private_facility',
            field=models.CharField(choices=[('not_sure', 'Not sure'), ('private_facility', 'Private facility'), ('state_local_facility', 'State or local facility'), ('federal_facility', 'Federal facility')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='public_or_private_healthcare',
            field=models.CharField(choices=[('not_sure', 'Not sure'), ('private_facility', 'Private facility'), ('state_local_facility', 'State or local facility'), ('federal_facility', 'Federal facility')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='public_or_private_school',
            field=models.CharField(choices=[('private', 'Private -- Schools or programs funded privately such as charter schools, magnet schools, or faith-based colleges'), ('not_sure', "I'm not sure"), ('public', 'Public -- Schools or programs funded by local, state, or the federal government')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='relationship',
            field=models.CharField(blank=True, choices=[('another', "I'm reporting on behalf of another person"), ('myself', "I'm reporting for myself"), ('undisclosed', 'I prefer not to disclose')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='respondent_state',
            field=models.CharField(blank=True, choices=[('SD', 'South Dakota '), ('HI', 'Hawaii '), ('MD', 'Maryland '), ('VI', 'Virgin Islands '), ('CT', 'Connecticut '), ('IL', 'Illinois '), ('MP', 'Northern Mariana Islands '), ('AE', 'Armed Forces Canada '), ('IA', 'Iowa '), ('VA', 'Virginia '), ('AR', 'Arkansas '), ('AA', 'Armed Forces Americas '), ('MS', 'Mississippi '), ('AE', 'Armed Forces Europe '), ('WA', 'Washington '), ('KS', 'Kansas '), ('ME', 'Maine '), ('MO', 'Missouri '), ('NE', 'Nebraska '), ('OK', 'Oklahoma '), ('KY', 'Kentucky '), ('AL', 'Alabama '), ('NJ', 'New Jersey '), ('SC', 'South Carolina '), ('TN', 'Tennessee '), ('OR', 'Oregon '), ('ID', 'Idaho '), ('IN', 'Indiana '), ('TX', 'Texas '), ('VT', 'Vermont '), ('DC', 'District of Columbia '), ('RI', 'Rhode Island '), ('WI', 'Wisconsin '), ('MN', 'Minnesota '), ('AS', 'American Samoa '), ('AK', 'Alaska '), ('MA', 'Massachusetts '), ('GA', 'Georgia '), ('NM', 'New Mexico '), ('WY', 'Wyoming '), ('AE', 'Armed Forces Africa '), ('AE', 'Armed Forces Middle East '), ('NV', 'Nevada '), ('ND', 'North Dakota '), ('MI', 'Michigan '), ('DE', 'Delaware '), ('OH', 'Ohio '), ('LA', 'Louisiana '), ('PR', 'Puerto Rico '), ('GU', 'Guam '), ('CO', 'Colorado '), ('FL', 'Florida '), ('NH', 'New Hampshire '), ('NC', 'North Carolina '), ('MT', 'Montana '), ('PA', 'Pennsylvania '), ('CA', 'California '), ('UT', 'Utah '), ('AZ', 'Arizona '), ('WV', 'West Virginia '), ('AP', 'Armed Forces Pacific '), ('NY', 'New York ')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='respondent_type',
            field=models.CharField(choices=[('other_public_official', 'Other public official (judge, voting official, or other government official)'), ('healthcare', 'Healthcare provider or staff'), ('school', 'Individual(s) from school or educational program (teacher, administrator, staff, or students)'), ('employer', 'Employer or potential employer'), ('police_corrections_staff', 'Police, prison guard, or other corrections staff'), ('lender', 'Bank or loaning service'), ('landlord', 'Landlord, leasing office, or home/rental provider')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='when',
            field=models.CharField(choices=[('last_3_years', 'Within the last 3 years'), ('greater_than_3_years', 'More than 3 years ago'), ('last_6_months', 'Within the last 6 months')], default=None, max_length=700),
        ),
        migrations.AlterField(
            model_name='report',
            name='who_reporting_for',
            field=models.CharField(choices=[('other_public_official', 'Other public official (judge, voting official, or other government official)'), ('healthcare', 'Healthcare provider or staff'), ('employer', 'Employer or potential employer'), ('police_corrections_staff', 'Police, prison guard, or other corrections staff'), ('Individual(s) from school or educational program (teacher, administrator, staff, or students)', 'Individual(s) from school or educational program (teacher, administrator, staff, or students)'), ('lender', 'Bank or loaning service'), ('landlord', 'Landlord, leasing office, or home/rental provider')], max_length=100),
        ),
    ]
