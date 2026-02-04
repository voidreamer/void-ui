import { forwardRef, type TextareaHTMLAttributes } from 'react'
import { cn } from '../../utils'

export interface TextAreaProps extends TextareaHTMLAttributes<HTMLTextAreaElement> {
  /** Show error styling */
  error?: boolean
}

export const TextArea = forwardRef<HTMLTextAreaElement, TextAreaProps>(
  ({ error, className, ...props }, ref) => {
    return (
      <textarea
        ref={ref}
        className={cn('void-textarea', error && 'void-input--error', className)}
        {...props}
      />
    )
  }
)

TextArea.displayName = 'TextArea'
