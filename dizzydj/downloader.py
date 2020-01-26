from selenium import webdriver
from bs4 import BeautifulSoup

import os
import time
import requests

done_titles, failed_titles = [], []


class Downloader:
	"""Converts YouTube videos to mp3 and downloads them to the specified directory

		Args:
			playlist (str): Playlist containing the videos that are converted to mp3
			driver_path (str): Path to chromedriver.exe Make sure to make it a raw string
			quality (str): Quality of downloaded mp3 in kbps. Valid values are-
				'320'
				'256'
				'192'
				'128'
			rename (boolean): Rename the downloaded mp3 files
	"""

	def __init__(self, playlist, chrome_path, quality, rename):
		self.playlist = playlist
		self.driver_path = chrome_path
		self.quality = quality
		self.rename = rename

	def _chrome_driver(self, link):
		driver = webdriver.Chrome(self.driver_path)
		driver.get(link)
		driver.maximize_window()

		return driver

	def links_downloader(self, links):
		global done_titles
		global failed_titles
		driver = self._chrome_driver('https://www.y2mate.com/en11/youtube-mp3')
		driver.implicitly_wait(15)

		for i in links:
			r = requests.get(i)
			soup = BeautifulSoup(r.content, features='html.parser')
			title = soup.title.string[:-10]

			try:
				driver.get('https://www.y2mate.com/en11/youtube-mp3')
				time.sleep(1)

				xp_link = driver.find_element_by_xpath('//input[@name="query"]')
				xp_link.send_keys(i)
				xp_start = driver.find_element_by_xpath('//button[@id="btn-submit"]')
				xp_start.click()
				xp_bitrate = driver.find_element_by_xpath('//button[@class="btn btn-default dropdown-toggle"]')
				xp_bitrate.click()
				xp_320 = driver.find_element_by_xpath('//a[text()="{} kbps"]'.format(self.quality))
				xp_320.click()
				xp_start = driver.find_element_by_xpath('//button[@class="btn btn-success"]')
				xp_start.click()

				element = driver.find_element_by_xpath('//div[@class="form-group has-success has-feedback"]/a')
				address = element.get_attribute('href')

				driver.get(address)

				done_titles.append(title)
				print('Done', i)
				print(title, end='\n\n')

			except:
				failed_titles.append(title)
				print('FAILED', i)
				print(title, end='\n\n')

		driver.close()

	def download(self):
		links = []
		driver = self._chrome_driver(self.playlist)

		xpath = '//a[@class="yt-simple-endpoint style-scope ytd-playlist-video-renderer"]'
		xp_links = driver.find_elements_by_xpath(xpath)
		for i in xp_links:
			links.append(i.get_attribute('href'))

		driver.close()
		self.links_downloader(links)

		if self.rename:
			self.rename_files()

	def rename_files(self):
		global done_titles

		data_dir = input('Enter directory of downloaded files: ')
		done_titles = sorted(done_titles, key=str.casefold)

		for i in os.listdir(data_dir):
			if i.split('.')[-1] == 'mp3' and 'y2mate' in i:
				os.rename(os.path.join(data_dir, i), os.path.join(data_dir, ' '.join(i[13:].split('_')[:-2]) + '.mp3'))

		present_titles = sorted(os.listdir(data_dir), key=str.casefold)

		for i in zip(done_titles, present_titles):
			print(i[-1], '-->', i[0])

		ch = input('Rename? [y] or [n]: ')

		if ch == 'y':
			for i, file in enumerate(present_titles):
				if ord(file[0]) > 96:
					try:
						os.rename(os.path.join(data_dir, file), os.path.join(data_dir, done_titles[i]) + '.mp3')
					except:
						print(done_titles[i])
