rule _Unknown_packer_06__bqgkou
{
	meta:
		description = "Unknown packer _06_"
	strings:
		$a = {FAB8????BE????33F00E172E??????BA????87E65B33DC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
