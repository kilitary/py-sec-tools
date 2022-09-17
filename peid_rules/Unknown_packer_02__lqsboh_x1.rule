rule _Unknown_packer_02__lqsboh
{
	meta:
		description = "Unknown packer _02_"
	strings:
		$a = {FA8CDE8CCF8EDF8EC783C7??BB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
