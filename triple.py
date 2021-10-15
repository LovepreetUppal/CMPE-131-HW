def tripler(func):
	def three(*args, **kwargs):
		used = func(*args, **kwargs)
		used = func(*args, **kwargs)
		used = func(*args, **kwargs)
		return used
	return three
