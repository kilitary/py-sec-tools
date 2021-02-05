rule _PE_SHiELD_0_2_jauulz
{
	meta:
		description = "PE_SHiELD 0_2"
	strings:
		$a = {60E800000000414E414B494E5D83ED06EB02EA04}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
