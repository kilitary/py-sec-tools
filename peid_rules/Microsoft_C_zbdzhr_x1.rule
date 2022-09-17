rule _Microsoft_C_zbdzhr
{
	meta:
		description = "Microsoft C"
	strings:
		$a = {B430CD213C0273??B8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
