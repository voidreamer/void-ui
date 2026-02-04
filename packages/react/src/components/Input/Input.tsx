import { forwardRef, type InputHTMLAttributes } from 'react'
import { cn } from '../../utils'

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  /** Input size */
  inputSize?: 'sm' | 'md' | 'lg'
  /** Show error styling */
  error?: boolean
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ inputSize = 'md', error, className, ...props }, ref) => {
    return (
      <input
        ref={ref}
        className={cn(
          'void-input',
          inputSize !== 'md' && `void-input--${inputSize}`,
          error && 'void-input--error',
          className,
        )}
        {...props}
      />
    )
  }
)

Input.displayName = 'Input'

/** Form group wrapper with label, hint, and error message */
export interface FormGroupProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Label text */
  label?: string
  /** Hint text below input */
  hint?: string
  /** Error message */
  error?: string
  /** HTML for attribute on label */
  htmlFor?: string
}

export const FormGroup = forwardRef<HTMLDivElement, FormGroupProps>(
  ({ label, hint, error, htmlFor, className, children, ...props }, ref) => (
    <div ref={ref} className={cn('void-form-group', className)} {...props}>
      {label && <label className="void-label" htmlFor={htmlFor}>{label}</label>}
      {children}
      {hint && !error && <span className="void-hint">{hint}</span>}
      {error && <span className="void-error">{error}</span>}
    </div>
  )
)

FormGroup.displayName = 'FormGroup'
