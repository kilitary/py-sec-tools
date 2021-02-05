rule _Microsoft_C_19881989__kbyzor
{
	meta:
		description = "Microsoft C _19881989_"
	strings:
		$a = {B430CD213C0273??CD20BF????8B??????2BF781??????72}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
