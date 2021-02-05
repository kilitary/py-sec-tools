rule _PC_Shrinker_v0_29_xfqiza
{
	meta:
		description = "PC Shrinker v0_29"
	strings:
		$a = {??BD????????01AD553940??8DB5353940}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
