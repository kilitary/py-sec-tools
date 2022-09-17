rule _PEtite_v1_4_vhlerr
{
	meta:
		description = "PEtite v1_4"
	strings:
		$a = {????????59F3A583C8FF8BDFAB40AB40}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
