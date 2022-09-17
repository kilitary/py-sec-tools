rule _REC_v0_34_3_iaawcf
{
	meta:
		description = "REC v0_34 _3"
	strings:
		$a = {061EB430CD213C0273??33C00650CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
