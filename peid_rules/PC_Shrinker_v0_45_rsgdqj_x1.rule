rule _PC_Shrinker_v0_45_rsgdqj
{
	meta:
		description = "PC Shrinker v0_45"
	strings:
		$a = {??BD????????01ADE33840??FFB5DF3840}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
