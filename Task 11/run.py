import numpy as np
from plotting import plt, plot_distributions, plot_pdf
from astropy.table import Table


from solution import resample_pdf_distribution, get_distribution


table = Table.read('data.fits')

starforming = table[table['SF']]
not_starforming = table[~table['SF']]

sample_size = 2000

starforming_choices = np.random.choice(len(starforming), size=sample_size)  # randomly sample from high_z
starforming_sample = starforming[starforming_choices]

pdf = get_distribution(starforming_sample['MASS_MEDIAN'])
not_starforming_choices = resample_pdf_distribution(pdf, not_starforming['MASS_MEDIAN'], sample_size)  # sample with the sample distribution as high_z
not_starforming_sample = not_starforming[not_starforming_choices]

ax = plot_distributions('MASS_MEDIAN', [not_starforming, starforming], ['non-SFG-all', 'SFG-all'], 'rb')
plot_pdf(ax, pdf)
ax = plot_distributions('MASS_MEDIAN', [not_starforming_sample, starforming_sample], ['non-SFG', 'SFG'], 'rb')
plot_pdf(ax, pdf)
plt.show()