rule _CC_v2_61_Beta_pnxyus
{
	meta:
		description = "CC v2_61 Beta"
	strings:
		$a = {BA????B430CD213C0273??33C00650CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
