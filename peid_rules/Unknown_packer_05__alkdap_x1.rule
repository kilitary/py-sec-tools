rule _Unknown_packer_05__alkdap
{
	meta:
		description = "Unknown packer _05_"
	strings:
		$a = {FABB????B9????87E5872703E3918ACB80E1??D3C49133E38727}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
