rule _EmbedPE_v1_24__cyclotron_pygwho
{
	meta:
		description = "EmbedPE v1_24 __ cyclotron"
	strings:
		$a = {83EC506068????????E8CBFF0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
